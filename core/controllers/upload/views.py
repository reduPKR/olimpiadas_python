import pandas as pd

from django.shortcuts import render
from django.contrib import messages
from core.models import *


def upload(request):
    if request.POST:
        athletes = request.FILES['athletes']
        regions = request.FILES['regions']

        if regions and athletes:
            df_regions = pd.read_csv(regions, ",")
            df_athletes = pd.read_csv(athletes, ",")
            save_data(df_athletes, df_regions, request)
        else:
            upload_message(regions, athletes, request)

    data = {
        'title': "Upload de arquivo"
    }

    return render(request, 'upload/upload.html', data)

def upload_message(regions, athletes, request):
    if regions is None:
        messages.error(request, "Arquivo nescessário: regiões")

    if athletes is None:
        messages.error(request, "Arquivo nescessário: atlétas")

def register_message(error, message, request):
    messages.error(request, "{}: {}".format(message, error))

def save_data(athletes, regions, request):
    save_region(regions, request)
    save_sports(athletes["Sport"], request)
    save_events(athletes[["Sport", "Event"]], request)
    save_city(athletes["City"], request)
    save_season(athletes["Season"], request)
    save_game(athletes[["Year", "Season", "City"]], request)
    save_game_event(athletes[["Year", "Season", "City", "Event"]], request)

def save_region(regions, request):
    regions.fillna(value="", inplace=True)

    message_except = "Erro ao salvar região"
    for item in regions.iterrows():
        if region_not_exist(item[1]["NOC"]):
            try:
                register_country(item[1])
            except:
                register_message(item[1]["NOC"], message_except, request)

def region_not_exist(noc):
    return Country.objects.filter(noc=noc).first() == None

def register_country(country):
    Country.objects.create(
            noc=country["NOC"],
            name=country["region"],
            notes=country["notes"]
        )

def save_sports(sport, request):
    df = sport.unique()

    message_except = "Erro ao cadastrar o esporte"
    for item in df:
        if sport_not_exist(item):
            try:
                register_sport(item)
            except:
                register_message(item, message_except, request)

def sport_not_exist(sport):
    return Sport.objects.filter(name=sport).first() == None

def get_sport_by_name(sport):
    return Sport.objects.get(name=sport)

def register_sport(sport):
    Sport.objects.create(
        name=sport
    )

def save_events(event, request):
    df = event.drop_duplicates('Event', keep='first')

    message_except = "Erro ao cadastrar o evento"
    for item in df.iterrows():
        #print("{} {}".format(item[1]["Sport"], item[1]["Event"]))
        if not sport_not_exist(item[1]["Sport"]):
            if event_not_exist(item[1]["Event"]):
                try:
                    register_event(item[1]["Event"], item[1]["Sport"])
                except:
                    register_message(item[1]["Event"], message_except, request)

def event_not_exist(event):
    return Event.objects.filter(name=event).first() == None

def get_event_by_name(event):
    return Event.objects.get(name=event)

def register_event(event, sport):
    Event.objects.create(
        name=event,
        sport= get_sport_by_name(sport)
    )

def save_city(city, request):
    df = city.unique()

    message_except = "Erro ao salvar a cidade"
    for item in df:
        if city_not_exist(item):
            try:
                register_city(item)
            except:
                register_message(item, message_except, request)

def city_not_exist(city):
    return City.objects.filter(name=city).first() == None

def get_city_by_name(city):
    return City.objects.get(name=city)

def register_city(city):
    City.objects.create(
        name=city
    )

def save_season(season, request):
    df = season.unique()

    message_except = "Erro ao cadastrar a temporada"
    for item in df:
        if season_not_exist(item):
            try:
                register_season(item)
            except:
                register_message(item, message_except, request)

def season_not_exist(season):
    return Season.objects.filter(name=season).first() == None

def get_season_by_name(season):
    return Season.objects.get(name=season)

def register_season(season):
    Season.objects.create(
        name=season
    )

def save_game(game, request):
    df = game.drop_duplicates(["Year", "Season", "City"], keep='first')

    message_except = "Erro ao cadastrar o jogo "
    for item in df.iterrows():
        if not season_not_exist(item[1]["Season"]):
            if not city_not_exist(item[1]["City"]):
                if game_not_exist(item[1]["Year"], item[1]["Season"], item[1]["City"]):
                    try:
                        register_game(item[1]["Year"], item[1]["Season"], item[1]["City"])
                    except:
                        register_message(item[1]["Year"]+" "+item[1]["Season"], message_except, request)

def game_not_exist(year, season, city):
    return Game.objects.filter(
        year=year,
        season= get_season_by_name(season),
        city=get_city_by_name(city)
    ).first() == None

def get_game_by_data(year, season, city):
    return Game.objects.get(
        year=year,
        season= get_season_by_name(season),
        city=get_city_by_name(city)
    )

def register_game(year, season, city):
    Game.objects.create(
        year=year,
        season= get_season_by_name(season),
        city= get_city_by_name(city)
    )

def save_game_event(game_event, request):
    df = game_event.drop_duplicates(["Year", "Season", "City", "Event"], keep='first')

    message_except = "Erro ao cadastrar evento nos jogos "
    for item in df.iterrows():
        if not event_not_exist(item[1]["Event"]):
            if not game_not_exist(item[1]["Year"], item[1]["Season"], item[1]["City"]):
                if game_event_not_exist(item[1]["Year"], item[1]["Season"], item[1]["City"], item[1]["Event"]):
                    try:
                        (item[1]["Year"], item[1]["Season"], item[1]["City"])
                    except:
                        register_message(item[1]["Event"], message_except, request)

def game_event_not_exist(year, season, city, event):
    return GameEvents.objects.filter(
        game=get_game_by_data(year, season, city),
        event=get_event_by_name(event)
    ).first() == None

def register_game_event(year, season, city, event):
    GameEvents.objects.create(
        game=get_game_by_data(year, season, city),
        event=get_event_by_name(event)
    )