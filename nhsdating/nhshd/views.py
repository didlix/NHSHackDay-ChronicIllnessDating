from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404


from models import Patient

def home(request):
    return TemplateResponse(request, 'home.html', {})


def profile(request, username):
    """
    Users profile page
    """

    patient = get_object_or_404(Patient, user__username=username)

    return TemplateResponse(request, 'profile.html', {"patient": patient})


def matches(request):
    """
    List of users who have things in common with request.user
    """
    return TemplateResponse(request, 'matches.html', {})
