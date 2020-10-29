from core import models
from core.dao import Medal, EventParticipants, GameEvent, Game, Athlete, Country, Sport


def list_all():
    return models.Athlete.objects.all().order_by('name')

def filter_by_team_id(team_id):
    return list(models.Athlete.objects.filter(team=team_id).order_by("name"))

def filter_by_sport_id(sport_id):
    return list(models.Athlete.objects.filter(sport=sport_id).order_by("name"))

def filter_by_sex(sex):
    return list(models.Athlete.objects.filter(sex=sex).order_by("name"))

def filter(name, age, height, weight, sex, team_id, game_id, event_id, sport_id, city_id, season_id, gold, silver, bronze):
    athletes = []
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

    if name != "" or age != "" or height != "" or weight != "":
        athletes = Athlete.filter_athletes(name, age, height, weight)

    return intersection(athletes, athletes_medal, athletes_team, athletes_sport, athletes_age, athletes_sex, athletes_event, athletes_games, athletes_city, athletes_season )



def filter_athletes(name, age, height, weight):
    list_name = []
    list_age = []
    list_height = []
    list_weight = []

    if name != "":
        list_name = list(models.Athlete.objects.filter(name__contains=name).order_by("name"))

    if age != "":
        list_age = list(models.Athlete.objects.filter(age=age).order_by("name"))

    if height != "":
        list_height = list(models.Athlete.objects.filter(height=height).order_by("name"))

    if weight != "":
        list_weight = list(models.Athlete.objects.filter(weight=weight).order_by("name"))

    return list_name+list_age+list_height+list_weight

def intersection(athletes, athletes_medal, athletes_team, athletes_sport, athletes_age, athletes_sex, athletes_event, athletes_games, athletes_city, athletes_season ):
    response = intersection_execute(athletes, athletes_medal)
    response = intersection_execute(response, athletes_team)
    response = intersection_execute(response, athletes_sport)
    response = intersection_execute(response, athletes_age)
    response = intersection_execute(response, athletes_sex)
    response = intersection_execute(response, athletes_event)
    response = intersection_execute(response, athletes_games)
    response = intersection_execute(response, athletes_city)
    response = intersection_execute(response, athletes_season)

    return response

def intersection_execute(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1

    return [value for value in list1 if value in list2]

def get_by_id(id):
    try:
        return models.Athlete.objects.get(id=id)
    except:
        return None

def get_all_info_by_id(id):
    athlete = get_by_id(id)
    athlete.events = EventParticipants.filter_by_athlete(athlete)

    return athlete


def delete(id):
    try:
        athlete = models.Athlete.objects.get(id=id)
        if athlete:
            athlete.delete()
            return True
    except:
        return False


def create(name, height, weight, sex, team_id, sport_id):
    try:
        return models.Athlete.objects.create(
            name=name,
            sex=sex,
            height=height,
            weight=weight,
            team= Country.get_by_id(team_id),
            sport= Sport.get_by_id(sport_id)
        )
    except:
        return None


def update(id, name, height, weight, sex, team_id, sport_id):
    try:
        return models.Athlete.objects.filter(id=id).update(
            name=name,
            sex=sex,
            height=height,
            weight=weight,
            team=Country.get_by_id(team_id),
            sport=Sport.get_by_id(sport_id)
        )
    except:
        return None