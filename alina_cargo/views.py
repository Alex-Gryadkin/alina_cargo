from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


def homepage(request):
    return render(request, 'home.html')
