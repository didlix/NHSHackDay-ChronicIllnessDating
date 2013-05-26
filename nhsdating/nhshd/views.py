# -*- encoding: utf8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django.db import models

from models import Patient, Message, Interest
from forms import MessageForm
import json
import models
from models import Patient, Message

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
    # Add three years either side.
    # Sort by gender first.

    patient = get_object_or_404(Patient, user__username=request.user.username)

    matches = Patient.objects.filter(
        other_conditions__in=patient.other_conditions.all()
    ).exclude(pk=patient.id).distinct()
    if request.GET.get("interest"):
        interest = get_object_or_404(Interest, name=request.GET["interest"])
        matches = matches.filter(interests=interest)
    return TemplateResponse(
        request, 'matches.html',
        {
            "matches": matches,
        }
    )
