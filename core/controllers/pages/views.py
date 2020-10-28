from django.shortcuts import render, redirect
from django.contrib import messages

import core.dao.Athlete as athlete
import core.dao.Country as country
import core.dao.Game as game
import core.dao.Event as event
import core.dao.Sport as sport
import core.dao.City as city
import core.dao.Season as season

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
        'city': city.list_all(),
        'season': season.list_all(),
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
        season_id = request.POST.get("season_id")
        gold = request.POST.get("gold")
        silver = request.POST.get("silver")
        bronze = request.POST.get("bronze")

        if filter_validate(name, age, height, weight, sex, team_id, game_id,
                           event_id, sport_id, city_id, season_id, gold, silver, bronze):

            data = {
                'title': "Lista de atletas",
                'athletes': athlete.filter(name, age, height, weight, sex, team_id, game_id,
                                            event_id, sport_id, city_id, season_id, gold, silver, bronze)
            }

            return render(request, 'athlete/list.html', data)
        else:
            messages.error(request, "Nenhum um filtro selecionado")

    return redirect('/athlete/filter')

def filter_validate(name, age, height, weight, sex, team_id, game_id, event_id, sport_id, city_id, season_id, gold, silver, bronze):
    if sex != "A":
        return True

    if name != "" or age != "" or height != "" or weight != "":
        return True

    if team_id != "0" or game_id != "0" or event_id != "0" or sport_id != "0" or city_id != "0" or season_id != "0":
        return True

    if gold is not None or silver is not None or bronze is not None:
        return True

    return False

def athlete_view(request):
    if request.GET and request.GET.get("id"):
        id = request.GET.get("id")

        data = {
            'title': "Visualizar atleta",
            'athlete': athlete.get_all_info_by_id(id)
        }

        return render(request, 'athlete/view.html', data)

    return redirect('/athlete/filter')