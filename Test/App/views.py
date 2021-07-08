from django.shortcuts import render
from django.views.generic import *
from .models import Formation
# Create your views here.

class Formation_ListView(ListView):
    model = Formation
    context_object_name = 'formations'
    