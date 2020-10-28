from core import models
from core.dao import Medal, EventParticipants


def list_all():
    return models.Athlete.objects.all().order_by('name')

def filter_by_team_id(team_id):
    return list(models.Athlete.objects.filter(team=team_id))

def filter_by_sport_id(sport_id):
    return list(models.Athlete.objects.filter(sport=sport_id))

def filter(name, age, height, weight, team_id, game_id, event_id, sport_id, city_id, gold, silver, bronze):
    athletes = []
    athletes_medal = []
    athletes_team = []
    athletes_sport = []

    if team_id is not "0":
        athletes_team = filter_by_team_id(team_id)

    if sport_id is not "0":
        athletes_sport = filter_by_sport_id(sport_id)

    if gold is not None or silver is not None or bronze is not None:
        medals = Medal.filter(gold, silver, bronze)
        athletes_medal = EventParticipants.filter_get_athlete_medals(medals)

    return athletes_sport