from core import models
import pandas as pd

def filter_by_medals(medals):
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
    athletes = []
    for game_event in game_events:
        participants = models.EventParticipant.objects.filter(game_event=game_event)

        if len(participants) > 0:
            for item in participants:
                athletes.append(item.athlete)

    return athletes

def filter_by_athlete(athlete):
    events = models.EventParticipant.objects.filter(athlete=athlete)

    if len(events) > 0:
        return list(events)
    return []

def create(athlete, age, game_event, medal):
    try:
        models.EventParticipant.objects.create(
            age=age,
            game_event= game_event,
            athlete= athlete,
            medal= medal,
        )
    except:
        return None

def delete(id):
    try:
        participant = models.EventParticipant.objects.get(id=id)
        if participant:
            participant.delete()
            return True
    except:
        return False

def get_registered_game_event_participant():
    participant = models.EventParticipant.objects.all()
    return pd.DataFrame(list(participant.values()))

def create(athlete, age, game_event, medal):
    return models.EventParticipant.objects.create(
        age=age,
        game_event=game_event,
        athlete=athlete,
        medal=medal
    )