from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django.db import models

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


def matches(request):
    """
    List of users who have things in common with request.user
    """

    patient = get_object_or_404(Patient, user__username=request.user.username)
    matches = Patient.objects.filter(
        other_conditions__in=patient.other_conditions.all()
    ).exclude(pk=patient.id).distinct()

    return TemplateResponse(
        request, 'matches.html',
        {"matches": matches}
    )
