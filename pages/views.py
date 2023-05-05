from django.shortcuts import render, get_object_or_404
from .models import Page, Category
from django.views.generic import View
from django.http import JsonResponse
from django.core.serializers import serialize


# Create your views here.
def page_view(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'page.html', {'page': page})

