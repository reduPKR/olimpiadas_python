from django.shortcuts import render, redirect

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

def athlete_filter_submit(request):
    if request.POST:
        name = request.POST.get("name")
        age = request.POST.get("age")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        sex = request.POST.get("sex")
        team_id = request.POST.get("team_id")
        game_id = request.POST.get("game_id")
        event_id = request.POST.get("event_id")
        sport_id = request.POST.get("sport_id")
        city_id = request.POST.get("city_id")
        gold = request.POST.get("gold")
        silver = request.POST.get("silver")
        bronze = request.POST.get("bronze")

        print("ouro {}".format(gold))
        print("prata {}".format(silver))
        print("bronze {}".format(bronze))
        data = {
            'title': "Lista de atletas",
            'athletes': athlete.list_all()
        }

        return render(request, 'athlete/list.html', data)
    return redirect('/athlete/filter')