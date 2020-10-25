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
    save_events(athletes[["Sport", "Event"]])

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
    return Sport.objects.get(name=sport).first()

def register_sport(sport):
    Sport.objects.create(
        name=sport
    )

def save_events(event):
    df = event.drop_duplicates('Event', keep='first')

    for item in df.iterrows():
        #print("{} {}".format(item[1]["Sport"], item[1]["Event"]))
        if not sport_not_exist(item[1]["Sport"]):
            if event_not_exist(item[1]["Event"]):
                register_event(item[1]["Event"], item[1]["Sport"])


def event_not_exist(event):
    return Event.objects.filter(name=event).first() == None

def register_event(event, sport):
    Event.objects.create(
        name=event,
        sport= get_sport_by_name(sport)
    )