import pandas as pd

from django.shortcuts import render
from django.contrib import messages



def upload(request):
    if request.POST:
        athletes = request.FILES['athletes']
        regions = request.FILES['regions']

        if regions and athletes:
            save_region(regions)
            #save_athletes(athletes)
        else:
            getMessage(regions, athletes, request)

    data = {
        'title': "Upload de arquivo"
    }

    return render(request, 'upload/upload.html', data)

def getMessage(regions, athletes, request):
    if regions is None:
        messages.error(request, "Arquivo nescessário: regiões")

    if athletes is None:
        messages.error(request, "Arquivo nescessário: atlétas")

def save_region(regions):
    df = pd.read_csv(regions, ",")

def save_athletes(athletes):
    df = pd.read_csv(athletes, ",")


