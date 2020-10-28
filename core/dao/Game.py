from core import models

def list_all():
    return models.Game.objects.all().order_by('year')


def filter_by_city(city_id):
    games = models.Game.objects.filter(city=city_id)

    if len(games) > 0:
        return list(games)

    return []