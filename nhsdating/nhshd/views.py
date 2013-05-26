from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django.db import models as django_models

from forms import MessageForm
import json
import models

from models import Patient, Message, Condition, Interest, Symptom
from matcher import sort_matches

from itertools import chain

def home(request):
    return TemplateResponse(request, 'home.html', {})


def your_profile(request):
    """
    Redirect to the profile of the logged in user
    """
    return HttpResponseRedirect(
        reverse('profile', kwargs={"username": request.user.username})
    )

def profile(request, username):
    """
    Users profile page
    """

    patient = get_object_or_404(Patient, user__username=username)

    return TemplateResponse(request, 'profile.html', {"patient": patient})


def inbox(request):
    #patient = get_object_or_404(Patient, user__username=request.user.username)

    messages = []
    senders = request.user.received_messages.distinct('sender').values_list('sender', flat=True)
    for sender in senders:
        latest = Message.objects.filter(sender=sender, receiver=request.user).order_by('-created_at')[0]
        messages.append(latest)
    messages.sort(key=lambda m: m.created_at, reverse=True)
    return TemplateResponse(request, 'inbox.html',
                            {"inbox": messages})


def conversation(request, sender_name):
    #patient = get_object_or_404(Patient, user__username=request.user.username)

    messages = Message.objects.filter(
        django_models.Q(sender__username=sender_name,
          receiver=request.user) |
        django_models.Q(receiver__username=sender_name,
          sender=request.user)
    ).order_by('-created_at')

    return TemplateResponse(request, 'convo.html',
                            {"convo": messages,
                            "sender": sender_name,
                            })


def send_message(request, username):
    recipient = get_object_or_404(Patient, user__username = username).user
    sender = request.user

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.sender_id = sender
            form.receiver_id = recipient
            message = Message(sender=sender, body=form.cleaned_data['body'], receiver=recipient)
            message.save()
            return HttpResponseRedirect(
                reverse('conversation', kwargs={"sender_name": message.receiver.username})
            )
    else:
        form = MessageForm()

    return TemplateResponse(request, 'send.html', {"form": form, "recipient": recipient})


def autocomplete(request, class_name):
    things = getattr(models, class_name).objects.filter(name__istartswith=request.GET['term'])

    return HttpResponse(
        json.dumps([{"id": t.id, "label": t.name} for t in things]),
        content_type="application/json"
    )

def matches(request):
    """
    List of users who have things in common with request.user
    """
    patient = get_object_or_404(Patient, user__username=request.user.username)

    def _resolve_by_name(model_cls, names_str):
        if names_str:
            results = []
            names = names_str.split(",")
            for name in names:
                results.extend(model_cls.objects.filter(name=name))
            return results
        else:
            return []

    interests = _resolve_by_name(Interest, request.GET.get('interest'))
    conditions = _resolve_by_name(Condition, request.GET.get('conditions'))
    symptoms = _resolve_by_name(Symptom, request.GET.get('symptom'))

    age_from = request.GET.get('min_age')
    age_to = request.GET.get('max_age')

    if request.GET.get('near_me'):
        locations = patient.locations.all()
    else:
        locations = _resolve_by_name(Symptom, request.GET.get('location'))

    print "Matching On:"
    print "Interests: %s" % interests
    print "Conditions: %s" % conditions
    print "Symptoms: %s" % symptoms
    print "Age from: %s" % age_from
    print "Age to: %s" % age_to
    print "Locations: %s" % locations

    base_matches = Patient.objects.all().exclude(user=request.user)

    matches = sort_matches(matches=base_matches,
                           interests=interests,
                           conditions=conditions,
                           symptoms=symptoms,
                           age_from=age_from,
                           age_to=age_to,
                           locations=locations,
                           )

    return TemplateResponse(
            request, 'matches.html',
            {
                "matches": matches,
                "init_conditions": request.GET.get('conditions') or ",".join(
                    chain(
                        [patient.primary_condition.name],
                        (c.name for c in patient.other_conditions.all())
                        )
                    ),
            "init_symptoms": request.GET.get('symptom') or ",".join(s.name for s in patient.symptoms.all()),
            "init_interests": request.GET.get('interest') or ",".join(i.name for i in patient.interests.all()),
            "near_me": request.GET.get('near_me')
            }
    )
