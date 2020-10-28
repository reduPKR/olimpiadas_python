from core import models
from core.dao import Medal, EventParticipants


def list_all():
    return models.Athlete.objects.all().order_by('name')

def filter(name, age, height, weight, team_id, game_id, event_id, sport_id, city_id, gold, silver, bronze):
    if gold is not None or silver is not None or bronze is not None:
        medals = Medal.filter(gold, silver, bronze)
        athletes = EventParticipants.filter_get_athlete(medals)

    return athletes