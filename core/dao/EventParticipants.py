from core import models

def filter(medals):
    participants = models.EventParticipant.objects.filter(medal__in=medals)

    if len(participants) > 0:
        return list(participants)
    return None

def filter_get_athlete_age(age):
    participants = models.EventParticipant.objects.filter(age=age)

    athletes = []
    if len(participants) > 0:
        for item in participants:
            athletes.append(item.athlete)

    return athletes

def filter_get_athlete_medals(medals):
    participants = models.EventParticipant.objects.filter(medal__in=medals)

    athletes = []
    if len(participants) > 0:
        for item in participants:
            athletes.append(item.athlete)

    return athletes

def filter_get_athlete_game_event(game_events):
    print(len(game_events))
    participants = models.EventParticipant.objects.filter(game_event__in=game_events)

    athletes = []
    if len(participants) > 0:
        for item in participants:
            athletes.append(item.athlete)

    return athletes