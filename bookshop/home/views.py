from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view


def home(request):
    return render(request, 'home/home.html')


def registration(request):
    render(request, 'home/registration.html')
