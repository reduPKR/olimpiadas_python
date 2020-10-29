from core import models
import pandas as pd

def list_all():
    return models.Game.objects.all().order_by('year')

def filter_by_city(city_id):
    games = models.Game.objects.filter(city=city_id)

    if len(games) > 0:
        return list(games)

    return []

def filter_by_season(season_id):
    seasons = models.Game.objects.filter(season=season_id)

    if len(seasons) > 0:
        return list(seasons)

    return []

def get_registered_games():
    games = models.Game.objects.all()
    return pd.DataFrame(list(games.values()))

def get_game_by_id(game_id):
    try:
        return models.Game.objects.get(id=game_id)
    except:
        return None

def create(year, season, city):
    return models.Game.objects.create(
        year=year,
        season=season,
        city=city
    )