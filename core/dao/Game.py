from core import models

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