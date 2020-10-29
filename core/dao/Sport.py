from core import models
import pandas as pd

def list_all():
    return models.Sport.objects.all().order_by('name')

def get_by_id(id):
    try:
        return models.Sport.objects.get(id=id)
    except:
        return None

def get_registered_sports():
    sports = models.Sport.objects.all()
    return pd.DataFrame(list(sports.values()))

def get_sport_by_name(sport):
    try:
        return models.Sport.objects.get(name=sport)
    except:
        return None

def create(sport):
    return models.Sport.objects.create(
        name=sport
    )