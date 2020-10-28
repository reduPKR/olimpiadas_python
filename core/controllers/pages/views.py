from django.shortcuts import render

import core.dao.athlete as athlete
import core.dao.country as country
import core.dao.game as game
import core.dao.event as event
import core.dao.sport as sport
import core.dao.city as city

def home(request):
    data = {
        'title': "Home"
    }

    return render(request, 'menu/home.html', data)

def upload(request):
    data = {
        'title': "Upload de arquivo"
    }

    return render(request, 'upload/upload.html', data)

def athlete_list(request):
    data = {
        'title': "Lista de atletas",
        'athletes': athlete.list_all()
    }

    return render(request, 'athlete/list.html', data)

def athlete_filter(request):
    data = {
        'title': "Filtrar atletas",
        'team': country.list_all(),
        'game': game.list_all(),
        'event': event.list_all(),
        'sport': sport.list_all(),
        'city': city.list_all()
    }

    return render(request, 'athlete/filter.html', data)