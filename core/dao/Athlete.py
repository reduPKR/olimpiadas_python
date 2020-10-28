from core import models
from core.dao import Medal, EventParticipants, GameEvent, Game


def list_all():
    return models.Athlete.objects.all().order_by('name')

def filter_by_team_id(team_id):
    return list(models.Athlete.objects.filter(team=team_id))

def filter_by_sport_id(sport_id):
    return list(models.Athlete.objects.filter(sport=sport_id))

def filter_by_sex(sex):
    return list(models.Athlete.objects.filter(sex=sex))

def filter(name, age, height, weight, sex, team_id, game_id, event_id, sport_id, city_id, season_id, gold, silver, bronze):
    athletes_medal = []
    athletes_team = []
    athletes_sport = []
    athletes_age = []
    athletes_sex = []
    athletes_event = []
    athletes_games = []
    athletes_city= []
    athletes_season = []

    if team_id != "0":
        athletes_team = filter_by_team_id(team_id)

    if sport_id != "0":
        athletes_sport = filter_by_sport_id(sport_id)

    if age != "":
        athletes_age = EventParticipants.filter_get_athlete_age(age)

    if sex != "A":
        athletes_sex = filter_by_sex(sex)

    if gold is not None or silver is not None or bronze is not None:
        medals = Medal.filter(gold, silver, bronze)
        athletes_medal = EventParticipants.filter_get_athlete_medals(medals)

    if event_id != "0":
        game_events = GameEvent.filter_by_event(event_id)
        athletes_event = EventParticipants.filter_get_athlete_game_event(game_events)

    if game_id != "0":
        game_events = GameEvent.filter_by_game_id(game_id)
        athletes_games = EventParticipants.filter_get_athlete_game_event(game_events)

    if city_id != "0":
        games = Game.filter_by_city(city_id)
        if len(games) > 0:
            game_events = GameEvent.filter_by_game(games)
            athletes_city = EventParticipants.filter_get_athlete_game_event(game_events)

    if season_id != "0":
        games = Game.filter_by_season(season_id)
        if len(games) > 0:
            game_events = GameEvent.filter_by_game(games)
            athletes_season = EventParticipants.filter_get_athlete_game_event(game_events)

    return athletes_games