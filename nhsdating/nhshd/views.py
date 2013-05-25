from django.http import HttpResponse
from django.template.response import TemplateResponse

def home(request):
    return TemplateResponse(request, 'home.html', {})


def matches(request):
    """
    List of users who have things in common with request.user
    """
    return TemplateResponse(request, 'matches.html', {})
