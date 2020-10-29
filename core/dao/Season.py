from core import models
import pandas as pd

def list_all():
    return models.Season.objects.all().order_by('name')

def get_registered_season():
    season = models.Season.objects.all()
    return pd.DataFrame(list(season.values()))

def get_season_by_name(season):
    try:
        return models.Season.objects.get(name=season)
    except:
        None

def create(season):
    return models.Season.objects.create(
        name=season
    )