import pandas as pd

from django.shortcuts import render
from django.contrib import messages


import time

from core.dao import Country, Sport, Event, City, Season, Game, GameEvent, Athlete, EventParticipants, Medal

def upload(request):
    if request.POST:
        athletes = request.FILES['athletes']
        regions = request.FILES['regions']

        if regions and athletes:
            df_regions = pd.read_csv(regions, ",")
            df_athletes = pd.read_csv(athletes, ",")
            save_data(df_athletes, df_regions, request)
        else:
            upload_message(regions, athletes, request)

    data = {
        'title': "Upload de arquivo"
    }

    return render(request, 'upload/upload.html', data)

def upload_message(regions, athletes, request):
    if regions is None:
        messages.error(request, "Arquivo nescessário: regiões")

    if athletes is None:
        messages.error(request, "Arquivo nescessário: atlétas")

def register_message(error, message, request):
    messages.error(request, "{}: {}".format(message, error))

def save_data(athletes, regions, request):
    save_region(regions, request)
    save_sports(athletes["Sport"], request)
    save_events(athletes[["Sport", "Event"]], request)
    save_city(athletes["City"], request)
    save_season(athletes["Season"], request)
    save_game(athletes[["Year", "Season", "City"]], request)
    save_game_event(athletes[["Year", "Season", "City", "Event"]], request)
    save_athlete(athletes[["ID", "Name", "Sex", "Height", "Weight", "NOC", "Sport"]], request)
    save_event_participants(athletes[["Name", "Sex", "Height", "Weight",  "NOC", "Sport", "Age", "Year", "Season", "City", "Event", "Medal"]], request)

def get_in_dataframe(name, column, registered):
    return registered.loc[registered[column] == name]["id"].values[0]

def save_region(regions, request):
    regions.fillna(value="", inplace=True)
    registered_regions = Country.get_registered_regions()

    message_except = "Erro ao salvar região"
    for item in regions.iterrows():
        if region_not_exist(item[1]["NOC"], registered_regions):
            try:
                Country.create(item[1]["NOC"], item[1]["region"], item[1]["notes"],)
                registered_regions = update_registered_regions(registered_regions, item[1])
            except:
                register_message(item[1]["NOC"], message_except, request)

def region_not_exist(noc, registered):
    if len(registered) == 0:
        return True
    return len(registered.loc[registered["noc"] == noc]) == 0

def update_registered_regions(registered, data):
    if len(registered) == 0:
        return Country.get_registered_regions()
    else:
        df = pd.DataFrame([[ 0,data["NOC"], data["region"], data["notes"]]], [0], ["id", "noc", "name", "notes"])
        return pd.concat([registered, df])

def save_sports(sport, request):
    df = sport.unique()
    registered_sports = Sport.get_registered_sports()

    message_except = "Erro ao cadastrar o esporte"
    for item in df:
        if sport_not_exist(item, registered_sports):
            try:
                Sport.create(item)
                registered_sports = update_registered_sports(registered_sports, item)
            except:
                register_message(item, message_except, request)

def sport_not_exist(sport,  registered):
    if len(registered) == 0:
        return True
    return len(registered.loc[registered["name"] == sport]) == 0

def update_registered_sports(registered, data):
    if len(registered) == 0:
        return Sport.get_registered_sports()
    else:
        df = pd.DataFrame([[0, data]], [0], ["id", "name"])
        return pd.concat([registered, df])

def save_events(event, request):
    df = event.drop_duplicates('Event', keep='first')
    registered_sports = Sport.get_registered_sports()
    registered_events = Event.get_registered_events()

    message_except = "Erro ao cadastrar o evento"
    for item in df.iterrows():
        if not sport_not_exist(item[1]["Sport"], registered_sports):
            if event_not_exist(item[1]["Event"], registered_events):

                try:
                    sport = Sport.get_sport_by_name(item[1]["Sport"])
                    Event.create(item[1]["Event"], sport)

                    sport = get_in_dataframe(item[1]["Sport"], "name", registered_sports)
                    registered_events = update_registered_event(registered_events, sport, item[1]["Event"])
                except:
                    register_message(item[1]["Event"], message_except, request)

def event_not_exist(event, registered):
    if len(registered) == 0:
        return True
    return len(registered.loc[registered["name"] == event]) == 0

def update_registered_event(registered, sport, data):
    if len(registered) == 0:
        return Event.get_registered_events()
    else:
        df = pd.DataFrame([[0, data, sport]], [0], ["id", "name", "sport_id"])
        return pd.concat([registered, df])

def save_city(city, request):
    df = city.unique()
    registered_city = City.get_registered_city()

    message_except = "Erro ao salvar a cidade"
    for item in df:
        if city_not_exist(item, registered_city):
            try:
                City.create(item)
                registered_city = update_registered_city(registered_city, item)
            except:
                register_message(item, message_except, request)

def city_not_exist(city, registered):
    if len(registered) == 0:
        return True
    return len(registered.loc[registered["name"] == city]) == 0

def update_registered_city(registered, data):
    if len(registered) == 0:
        return City.get_registered_city()
    else:
        df = pd.DataFrame([[0, data]], [0], ["id", "name"])
        return pd.concat([registered, df])

def save_season(season, request):
    df = season.unique()
    registered_season = Season.get_registered_season()

    message_except = "Erro ao cadastrar a temporada"
    for item in df:
        if season_not_exist(item, registered_season):
            try:
                Season.create(item)
                registered_season = update_registered_season(registered_season, item)
            except:
                register_message(item, message_except, request)

def season_not_exist(season, registered):
    if len(registered) == 0:
        return True
    return len(registered.loc[registered["name"] == season]) == 0

def update_registered_season(registered, data):
    if len(registered) == 0:
        return Season.get_registered_season()
    else:
        df = pd.DataFrame([[0, data]], [0], ["id", "name"])
        return pd.concat([registered, df])

def save_game(game, request):
    df = game.drop_duplicates(["Year", "Season", "City"], keep='first')
    registered_season = Season.get_registered_season()
    registered_city = City.get_registered_city()
    registered_games = Game.get_registered_games()

    message_except = "Erro ao cadastrar o jogo "
    for item in df.iterrows():
        if not season_not_exist(item[1]["Season"], registered_season):
            if not city_not_exist(item[1]["City"], registered_city):

                season_id = get_in_dataframe(item[1]["Season"], "name", registered_season)
                city_id = get_in_dataframe(item[1]["City"], "name", registered_city)

                if game_not_exist(item[1]["Year"], season_id, city_id, registered_games):
                    try:
                        season = Season.get_season_by_name(item[1]["Season"])
                        city = City.get_city_by_name(item[1]["City"])
                        Game.create(item[1]["Year"], season, city)
                        registered_games = update_registered_game(registered_games, item[1]["Year"], season_id, city_id)
                    except:
                        register_message(item[1]["Year"]+" "+item[1]["Season"], message_except, request)

def game_not_exist(year, season, city, registered):
    if len(registered) == 0:
        return True
    return len(registered.loc[((registered["year"] == year) & (registered["city_id"] == city) & (registered["season_id"] == season))]) == 0

def get_game_by_data(year, season_id, city_id, registered):
    return registered.loc[((registered["year"] == year) &
                           (registered["city_id"] == city_id) &
                           (registered["season_id"] == season_id))]["id"].values[0]

def update_registered_game(registered, year, season, city):
    if len(registered) == 0:
        return Game.get_registered_games()
    else:
        df = pd.DataFrame([[0, year, city, season]], [0], ["id", "year", "city_id", "season_id"])
        return pd.concat([registered, df])

def save_game_event(game_event, request):
    df = game_event.drop_duplicates(["Year", "Season", "City", "Event"], keep='first')
    registered_season = Season.get_registered_season()
    registered_city = City.get_registered_city()
    registered_events = Event.get_registered_events()
    registered_games = Game.get_registered_games()
    registered_game_event = GameEvent.get_registered_games_event()

    message_except = "Erro ao cadastrar evento nos jogos "
    for item in df.iterrows():
        if not event_not_exist(item[1]["Event"], registered_events):

            season_id = get_in_dataframe(item[1]["Season"], "name", registered_season)
            city_id = get_in_dataframe(item[1]["City"], "name", registered_city)

            if not game_not_exist(item[1]["Year"], season_id, city_id, registered_games):

                event_id = get_in_dataframe(item[1]["Event"],"name", registered_events)
                game_id = get_game_by_data(item[1]["Year"], season_id, city_id, registered_games)

                if game_event_not_exist(game_id, event_id, registered_game_event):
                    try:
                        game = Game.get_game_by_id(game_id)
                        event = Event.get_event_by_id(event_id)
                        GameEvent.create(game, event)
                        registered_game_event = update_registered_game_event(registered_game_event, game_id, event_id)
                    except:
                        register_message(item[1]["Event"], message_except, request)

def get_game_event_in_dataframe(game_id, event_id, registered):
    if len(registered) == 0:
        return True
    return registered.loc[((registered["game_id"] == game_id) & (registered["event_id"] == event_id))]["id"].values[0]

def game_event_not_exist(game_id, event_id, registered):
    if len(registered) == 0:
        return True
    return len(registered.loc[((registered["game_id"] == game_id) & (registered["event_id"] == event_id))]) == 0

def update_registered_game_event(registered, game_id, event_id):
    if len(registered) == 0:
        return GameEvent.get_registered_games_event()
    else:
        df = pd.DataFrame([[0, game_id, event_id]], [0], ["id", "game_id", "event_id"])
        return pd.concat([registered, df])

def save_athlete(athlete, request):
    df = athlete.drop_duplicates("ID", keep='first')
    df[['Name', 'Sex']].fillna(value=" ", inplace=True)
    df['Height'].fillna(value=df['Height'].mean(), inplace=True)
    df['Weight'].fillna(value=df['Weight'].mean(), inplace=True)

    registered_country = Country.get_registered_regions()
    registered_sport = Sport.get_registered_sports()
    registered_athlete = Athlete.get_registered_athlete()

    message_except = "Erro ao cadastrar o atleta "
    for item in df.iterrows():
        if not region_not_exist(item[1]["NOC"], registered_country):
            if not sport_not_exist(item[1]["Sport"], registered_sport):

                sport_id = get_in_dataframe(item[1]["Sport"], "name", registered_sport)
                team_id = get_in_dataframe(item[1]["NOC"], "noc", registered_country)

                if athlete_not_exist(item[1]["Name"],item[1]["Sex"],
                                     item[1]["Height"],item[1]["Weight"],
                                     team_id, sport_id, registered_athlete):
                    try:
                        Athlete.create(item[1]["Name"], item[1]["Height"],item[1]["Weight"],
                                       item[1]["Sex"],team_id, sport_id)

                        registered_athlete = update_registered_athlete(registered_athlete, item[1]["Name"],
                                                                    item[1]["Sex"],item[1]["Height"],
                                                                    item[1]["Weight"],team_id,
                                                                    sport_id)
                    except:
                        register_message(item[1]["ID"]+" "+item[1]["Name"], message_except, request)

def athlete_not_exist(name, sex, height, weight, team_id, sport_id, registered):
    if len(registered) == 0:
        return True
    return len(registered.loc[((registered["name"] == name) & (registered["sex"] == sex) &
                               (registered["height"] == height) & (registered["weight"] == weight) &
                               (registered["team_id"] == team_id) & (registered["sport_id"] == sport_id))]) == 0

def get_athlete_id_in_dataframe(name, sex, height, weight, team_id, sport_id, registered):
    return registered.loc[((registered["name"] == name) & (registered["sex"] == sex) &
                    (registered["height"] == height) & (registered["weight"] == weight) &
                    (registered["team_id"] == team_id) & (registered["sport_id"] == sport_id))]["id"].values[0]

def update_registered_athlete(registered, name, sex, height, weight, team_id, sport_id):
    if len(registered) == 0:
        return Athlete.get_registered_athlete()
    else:
        df = pd.DataFrame([[0, name, height, weight, sex, team_id, sport_id]], [0],
                          ["id", "name", "height", "weight", "sex", "team_id", "sport_id"])
        return pd.concat([registered, df])

def save_event_participants(athlete, request):
    athlete[['Name', 'Sex', 'Medal']].fillna(value="", inplace=True)
    athlete['Height'].fillna(value=athlete['Height'].mean(), inplace=True)
    athlete['Weight'].fillna(value=athlete['Weight'].mean(), inplace=True)
    athlete['Age'].fillna(value=athlete['Age'].mean(), inplace=True)
    athlete.sort_values("Name", inplace=True)

    registered_country = Country.get_registered_regions()
    registered_sport = Sport.get_registered_sports()
    registered_athlete = Athlete.get_registered_athlete()
    registered_season = Season.get_registered_season()
    registered_city = City.get_registered_city()
    registered_events = Event.get_registered_events()
    registered_games = Game.get_registered_games()
    registered_game_event = GameEvent.get_registered_games_event()
    registered_participant = EventParticipants.get_registered_game_event_participant()

    message_except = "Erro ao cadastrar o atleta no evento"
    for item in athlete.iterrows():
        if not region_not_exist(item[1]["NOC"], registered_country):
            if not sport_not_exist(item[1]["Sport"], registered_sport):

                season_id = get_in_dataframe(item[1]["Season"], "name", registered_season)
                city_id = get_in_dataframe(item[1]["City"], "name", registered_city)
                event_id = get_in_dataframe(item[1]["Event"], "name", registered_events)
                game_id = get_game_by_data(item[1]["Year"], season_id, city_id, registered_games)

                if not game_event_not_exist(game_id, event_id, registered_game_event):

                    sport_id = get_in_dataframe(item[1]["Sport"], "name", registered_sport)
                    team_id = get_in_dataframe(item[1]["NOC"], "noc", registered_country)

                    if not athlete_not_exist(item[1]["Name"],item[1]["Sex"],  item[1]["Height"],item[1]["Weight"], team_id, sport_id, registered_athlete):

                        athlete_id = get_athlete_id_in_dataframe(item[1]["Name"],item[1]["Sex"],  item[1]["Height"],item[1]["Weight"], team_id, sport_id, registered_athlete)
                        game_event_id = get_game_event_in_dataframe(game_id,event_id, registered_game_event)

                        if event_participant_not_exist(athlete_id, item[1]["Age"], game_event_id, registered_participant):
                            try:
                                game_event = GameEvent.get_game_event_by_id(game_event_id)
                                athlete = Athlete.get_by_id(athlete_id)
                                medal = Medal.get_medal(item[1]["Medal"])
                                EventParticipants.create(athlete, item[1]["Age"], game_event, medal)
                                registered_participant = update_registered_participant(registered_athlete, athlete_id,
                                                                                       item[1]["Age"], game_event_id)
                            except:
                                register_message(item[1]["Name"]+" "+item[1]["Event"], message_except, request)

def event_participant_not_exist(athlete_id, age,  game_event_id, registered):
    if len(registered) == 0:
        return True
    return len(registered.loc[((registered["athlete_id"] == athlete_id) & (registered["age"] == age) &
                               (registered["game_event_id"] == game_event_id))]) == 0

def update_registered_participant(registered, athlete_id, age, game_event_id):
    if len(registered) == 0:
        return EventParticipants.get_registered_game_event_participant()
    else:
        df = pd.DataFrame([[0, athlete_id, age, game_event_id, 0]], [0],
                          ["id", "athlete_id", "age", "game_event_id", "medal_id"])
        return pd.concat([registered, df])
