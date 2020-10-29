from core import models

def filter_by_event(event_id):
    game_events = models.GameEvents.objects.filter(event=event_id)

    if len(game_events) > 0:
        return list(game_events)

    return []

def filter_by_game_id(game_id):
    game_events = models.GameEvents.objects.filter(game=game_id)
    if len(game_events) > 0:
        return list(game_events)

    return []

def filter_by_game(games):
    game_events = models.GameEvents.objects.filter(game__in=games)
    if len(game_events) > 0:
        return list(game_events)

    return []

def get_all():
    game_events = models.GameEvents.objects.all()
    if len(game_events) > 0:
        return list(game_events)

    return []


def get_did_not_participate(participants):
    game_events = list(models.GameEvents.objects.all())
    new_list = diference(participants, game_events)
    return sorted(new_list, key=lambda k: (k.game.year, k.event.name))


def diference(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1

    return [value for value in list2 if value not in list1]


def get_by_id(id):
    try:
        return models.GameEvents.objects.get(id=id)
    except:
        return None
