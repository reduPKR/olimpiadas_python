from django.shortcuts import render, redirect
from django.contrib import messages

import core.dao.Athlete as Athlete
import core.dao.Country as Country
import core.dao.Game as Game
import core.dao.Event as Event
import core.dao.Sport as Sport
import core.dao.City as City
import core.dao.Season as Season
from core.dao import GameEvent, EventParticipants, Medal


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
        'athletes': Athlete.list_all()
    }

    return render(request, 'athlete/list.html', data)

def athlete_filter(request):
    data = {
        'title': "Filtrar atletas",
        'team': Country.list_all(),
        'game': Game.list_all(),
        'event': Event.list_all(),
        'sport': Sport.list_all(),
        'city': City.list_all(),
        'season': Season.list_all(),
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
                'athletes': Athlete.filter(name, age, height, weight, sex, team_id, game_id,
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
            'athlete': Athlete.get_all_info_by_id(id)
        }

        return render(request, 'athlete/view.html', data)

    return redirect('/athlete/filter')

def athlete_delete(request,id):
    if id:
        if Athlete.delete(id) is False:
            messages.error(request, "Erro durante a exclusão")
        return redirect("/athlete/list/")
    else:
        messages.error(request, "Atleta nao encontrado")

def create_athlete(request):
    data = {
        'title': "Cadastrar atleta",
        'title_h': "Cadastro",
        'athlete': None,
        'team': Country.list_all(),
        'sport': Sport.list_all(),
    }

    return render(request, 'athlete/create.html', data)

def create_athlete_submit(request):
    if request.POST:
        name = request.POST.get("name")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        sex = request.POST.get("sex")
        team_id = request.POST.get("team_id")
        sport_id = request.POST.get("sport_id")

        if create_athlete_validate(name, height, weight):
            athlete = Athlete.create(name, height, weight, sex, team_id, sport_id )

            if athlete is None:
                messages.error(request, "Erro no cadastro")
            else:
                return redirect("/athlete/view/?id={}".format(athlete.id))
        else:
            message_error(name, height, weight, request)

        return redirect('/athlete/create')
    else:
        messages.error(request, "Erro no post")

def create_athlete_validate(name, height, weight):
    if name != "" and height != "" and weight != "":
        return True

    return False

def message_error(name, height, weight, request):
    if name != "":
        messages.error(request, "* Nome não pode estar vazio")
    if height != "":
        messages.error(request, "* Altura não pode estar vazia")
    if weight != "":
        messages.error(request, "* Peso não pode estar vazio")

def update_athlete(request, id):
    if id:
        data = {
            'title': "Alterar atleta",
            'title_h': "Atualização",
            'athlete': Athlete.get_by_id(id),
            'team': Country.list_all(),
            'sport': Sport.list_all(),
        }

    return render(request, 'athlete/create.html', data)

def update_athlete_submit(request):
    if request.POST and request.POST.get("id"):
        id = request.POST.get("id")
        name = request.POST.get("name")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        sex = request.POST.get("sex")
        team_id = request.POST.get("team_id")
        sport_id = request.POST.get("sport_id")

        if create_athlete_validate(name, height, weight):
            athlete = Athlete.update(id, name, height, weight, sex, team_id, sport_id)

            if athlete is None:
                messages.error(request, "Erro na atualização")
            else:
                return redirect("/athlete/view/?id={}".format(id))
        else:
            message_error(name, height, weight, request)

        return redirect('/athlete/update/{}'.format(id))
    else:
        messages.error(request, "Erro no post")

    return redirect('/athlete/filter')

def add_participation(request, id):
    if id:

        athlete = Athlete.get_by_id(id)
        participants = EventParticipants.filter_by_athlete(athlete)
        games_events = GameEvent.get_did_not_participate(participants)

        data = {
            'title': "Adicionar participacao em evento",
            'athlete':athlete,
            'games_events': games_events
        }

        return render(request, 'athlete/participation.html', data)

    return redirect("/athlete/filter/")


def participation_athlete_submit(request):
    if request.POST and request.POST.get("id"):
        id = request.POST.get("id")
        age = request.POST.get("age")
        game_event_id = request.POST.get("game_event_id")
        medal_id = request.POST.get("medal_id")

        if age != "":
            athlete = Athlete.get_by_id(id)
            game_event = GameEvent.get_by_id(game_event_id)
            medal = Medal.get_by_id(medal_id)

            EventParticipants.create(athlete, age, game_event, medal)
        else:
            messages.error(request, "* Idade não pode estar vazia")

    return redirect("/athlete/filter/")