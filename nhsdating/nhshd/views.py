from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django.db import models

from models import Patient, Message, Interest
from forms import MessageForm

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
        models.Q(sender__username=sender_name,
          receiver=request.user) |
        models.Q(receiver__username=sender_name,
          sender=request.user)
    ).order_by('-created_at')

    return TemplateResponse(request, 'convo.html',
                            {"convo": messages})

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
                reverse('conversation', kwargs={"sender_name": message.sender.username})
            )
    else:
        form = MessageForm()

    return TemplateResponse(request, 'send.html', {"form": form, "recipient": recipient})


def _generate_matches(interests, conditions, symptoms, age_from, age_to,locations):
    matches = Patient.objects.all()
    return matches


def search(request):

    # TODO: Kill me.
    interests = []
    if request.GET.get('interests'):
        names = request.GET.get('interests').split(",")
        interests = [get_object_or_404(Interest, name=name) for name in names]

    conditions = []
    if request.GET.get('conditions'):
        names = request.GET.get('conditions').split(",")
        conditions = [get_object_or_404(Condition, name=name) for name in names]

    symptoms = []
    if request.GET.get('symptoms'):
        names = request.GET.get('symptoms').split(",")
        symptoms = [get_object_or_404(Symptom, name=name) for name in names]

    locations = []
    if request.GET.get('locations'):
        names = request.GET.get('locations').split(",")
        locations = [get_object_or_404(Location, name=name) for name in names]

    age_from = request.GET.get('age_from')
    age_to = request.GET.get('age_to')

    matches = _generate_matches(interests=interests,
                                conditions=conditions,
                                symptoms=symptoms,
                                age_from=age_from,
                                age_to=age_to,
                                locations=locations
                                )

    return TemplateResponse(
        request, 'matches.html',
        {"matches": matches}
    )
    return TemplateResponse()


def matches(request):
    """
    List of users who have things in common with request.user
    """
    # Add three years either side.
    # Sort by gender first.

    patient = get_object_or_404(Patient, user__username=request.user.username)

    matches = _generate_matches(interests=patient.interests.all,
                                conditions=patient.conditions.all,
                                symptoms=patient.symptoms.all,
                                age_from=patient.age -3,
                                age_to=patient.age + 3,
                                locations=patient.locations.all
                                )

    return TemplateResponse(request, 'matches.html', {"matches": matches})
