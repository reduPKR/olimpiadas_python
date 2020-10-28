from core import models

def filter_by_event(event_id):
    game_events = models.GameEvents.objects.filter(event=event_id)

    if len(game_events) > 0:
        return list(game_events)

    return []