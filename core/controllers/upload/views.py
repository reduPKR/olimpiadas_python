import csv, io

from django.shortcuts import render
from django.contrib import messages


def upload(request):
    if request.POST:
        athletes = request.FILES['athletes']
        regions = request.FILES['regions']

        if regions and athletes:
            with open(athletes, newline='', encoding='utf-8') as f:
                csv_file = csv.reader(f)
                for row in csv_file:
                    print(row)

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