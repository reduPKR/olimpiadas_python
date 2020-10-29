from core import models

def filter_by_medals(medals):
    participants = models.EventParticipant.objects.filter(medal__in=medals).order_by("name")

    if len(participants) > 0:
        return list(participants)
    return None

def filter_get_athlete_age(age):
    participants = models.EventParticipant.objects.filter(age=age).order_by("name")

    athletes = []
    if len(participants) > 0:
        for item in participants:
            athletes.append(item.athlete)

    return athletes

def filter_get_athlete_medals(medals):
    participants = models.EventParticipant.objects.filter(medal__in=medals).order_by("name")

    athletes = []
    if len(participants) > 0:
        for item in participants:
            athletes.append(item.athlete)

    return athletes

def filter_get_athlete_game_event(game_events):
    athletes = []
    for game_event in game_events:
        participants = models.EventParticipant.objects.filter(game_event=game_event).order_by("name")

        if len(participants) > 0:
            for item in participants:
                athletes.append(item.athlete)

    return athletes


def filter_by_athlete(athlete):
    events = models.EventParticipant.objects.filter(athlete=athlete).order_by("name")

    if len(events) > 0:
        return list(events)
    return []