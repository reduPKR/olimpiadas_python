from django.shortcuts import render
from core.models import *

def menu_home(request):
    data = {
        'title': "Home"
    }

    return render(request, 'menu/home.html', data)