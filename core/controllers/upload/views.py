import pandas as pd

from django.shortcuts import render
from django.contrib import messages
from core.models import *



def upload(request):
    if request.POST:
        athletes = request.FILES['athletes']
        regions = request.FILES['regions']

        if regions and athletes:
            save_region(regions, request)
            #save_athletes(athletes)
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

def save_region(regions, request):
    df = pd.read_csv(regions, ",")
    df.fillna(value="", inplace=True)

    message_except = "Erro ao salvar região"
    for item in df.iterrows():
        if region_not_exist(item[1]["NOC"]):
            try:
                register_country(item[1])
            except:
                register_message(item[1]["NOC"], message_except, request)

def save_athletes(athletes):
    df = pd.read_csv(athletes, ",")

def region_not_exist(noc):
    return Country.objects.filter(noc=noc).first() == None

def register_country(country):
    Country.objects.create(
            noc=country["NOC"],
            region=country["region"],
            notes=country["notes"],
        )

def register_message(error, message, request):
    messages.error(request, "{}: {}".format(message, error))