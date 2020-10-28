from django.shortcuts import render
from django.contrib import messages
from core import models

def list_all():
    return models.Athlete.objects.all().order_by('name')
