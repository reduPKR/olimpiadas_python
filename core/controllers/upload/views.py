import pandas as pd

from django.shortcuts import render
from django.contrib import messages
from core.models import *


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
    # save_season(athletes["Season"], request)
    # save_game(athletes[["Year", "Season", "City"]], request)
    # save_game_event(athletes[["Year", "Season", "City", "Event"]], request)
    # save_athlete(athletes[["ID", "Name", "Sex", "Height", "Weight", "NOC", "Sport"]], request)
    # save_event_participants(athletes[["Name", "Sex", "Height", "Weight",  "NOC", "Sport", "Age", "Year", "Season", "City", "Event", "Medal"]], request)

def save_region(regions, request):
    regions.fillna(value="", inplace=True)
    registered_regions = get_registered_regions()

    message_except = "Erro ao salvar região"
    for item in regions.iterrows():
        if region_not_exist(item[1]["NOC"], registered_regions):
            try:
                register_country(item[1])
                registered_regions = update_registered_regions(registered_regions, item[1])
            except:
                register_message(item[1]["NOC"], message_except, request)

def get_registered_regions():
    regions = Country.objects.all()
    return pd.DataFrame(list(regions.values()))

def region_not_exist(noc, registered):
    if len(registered) == 0:
        return True
    return len(registered.loc[registered["noc"] == noc]) == 0

def update_registered_regions(registered, data):
    if len(registered) == 0:
        return get_registered_regions()
    else:
        df = pd.DataFrame([[ 0,data["NOC"], data["region"], data["notes"]]], [0], ["id", "noc", "region", "notes"])
        return pd.concat([registered, df])

def get_region_by_noc(noc):
    return Country.objects.get(noc=noc)

def register_country(country):
    Country.objects.create(
            noc=country["NOC"],
            name=country["region"],
            notes=country["notes"]
        )

def save_sports(sport, request):
    df = sport.unique()
    registered_sports = get_registered_sports()

    message_except = "Erro ao cadastrar o esporte"
    for item in df:
        if sport_not_exist(item, registered_sports):
            try:
                register_sport(item)
                registered_sports = update_registered_sports(registered_sports, item)
            except:
                register_message(item, message_except, request)

def get_registered_sports():
    sports = Sport.objects.all()
    return pd.DataFrame(list(sports.values()))

def sport_not_exist(sport,  registered):
    if len(registered) == 0:
        return True
    return len(registered.loc[registered["name"] == sport]) == 0

def update_registered_sports(registered, data):
    if len(registered) == 0:
        return get_registered_sports()
    else:
        df = pd.DataFrame([[0, data]], [0], ["id", "name"])
        return pd.concat([registered, df])

def get_sport_by_name(sport):
    return Sport.objects.get(name=sport)

def get_sport_by_name_in_dataframe(sport, registered):
    return registered.loc[registered["name"] == sport]["id"].values

def register_sport(sport):
    Sport.objects.create(
        name=sport
    )

def save_events(event, request):
    df = event.drop_duplicates('Event', keep='first')
    registered_sports = get_registered_sports()
    registered_events = get_registered_events()

    message_except = "Erro ao cadastrar o evento"
    for item in df.iterrows():
        if not sport_not_exist(item[1]["Sport"], registered_sports):
            if event_not_exist(item[1]["Event"], registered_events):
                try:
                    register_event(item[1]["Event"], item[1]["Sport"])
                    sport = get_sport_by_name_in_dataframe(item[1]["Sport"], registered_sports)
                    print(sport)
                    registered_events = update_registered_event(registered_events, sport, item[1]["Event"])
                except:
                    register_message(item[1]["Event"], message_except, request)

def get_registered_events():
    events = Event.objects.all()
    return pd.DataFrame(list(events.values()))

def event_not_exist(event, registered):
    if len(registered) == 0:
        return True
    return len(registered.loc[registered["name"] == event]) == 0

def get_event_by_name(event):
    return Event.objects.get(name=event)

def update_registered_event(registered, sport, data):
    if len(registered) == 0:
        return get_registered_events()
    else:
        df = pd.DataFrame([[0, data, sport]], [0], ["id", "name", "sport_id"])
        return pd.concat([registered, df])

def register_event(event, sport):
    Event.objects.create(
        name=event,
        sport= get_sport_by_name(sport)
    )

def save_city(city, request):
    df = city.unique()
    registered_city = get_registered_city()
    print(registered_city)

    message_except = "Erro ao salvar a cidade"
    for item in df:
        if city_not_exist(item, registered_city):
            try:
                register_city(item)
                registered_city = update_registered_city(registered_city, item)
                print(registered_city)
            except:
                register_message(item, message_except, request)

def get_registered_city():
    city = City.objects.all()
    return pd.DataFrame(list(city.values()))

def city_not_exist(city, registered):
    if len(registered) == 0:
        return True
    return len(registered.loc[registered["name"] == city]) == 0

def get_city_by_name(city):
    return City.objects.get(name=city)

def update_registered_city(registered, data):
    if len(registered) == 0:
        return get_registered_city()
    else:
        df = pd.DataFrame([[0, data]], [0], ["id", "name"])
        return pd.concat([registered, df])

def register_city(city):
    City.objects.create(
        name=city
    )

def save_season(season, request):
    df = season.unique()

    message_except = "Erro ao cadastrar a temporada"
    for item in df:
        if season_not_exist(item):
            try:
                register_season(item)
            except:
                register_message(item, message_except, request)

def season_not_exist(season):
    return Season.objects.filter(name=season).first() == None

def get_season_by_name(season):
    return Season.objects.get(name=season)

def register_season(season):
    Season.objects.create(
        name=season
    )

def save_game(game, request):
    df = game.drop_duplicates(["Year", "Season", "City"], keep='first')

    message_except = "Erro ao cadastrar o jogo "
    for item in df.iterrows():
        if not season_not_exist(item[1]["Season"]):
            if not city_not_exist(item[1]["City"]):
                if game_not_exist(item[1]["Year"], item[1]["Season"], item[1]["City"]):
                    try:
                        register_game(item[1]["Year"], item[1]["Season"], item[1]["City"])
                    except:
                        register_message(item[1]["Year"]+" "+item[1]["Season"], message_except, request)

def game_not_exist(year, season, city):
    return Game.objects.filter(
        year=year,
        season= get_season_by_name(season),
        city=get_city_by_name(city)
    ).first() == None

def get_game_by_data(year, season, city):
    return Game.objects.get(
        year=year,
        season= get_season_by_name(season),
        city=get_city_by_name(city)
    )

def register_game(year, season, city):
    Game.objects.create(
        year=year,
        season= get_season_by_name(season),
        city= get_city_by_name(city)
    )

def save_game_event(game_event, request):
    df = game_event.drop_duplicates(["Year", "Season", "City", "Event"], keep='first')

    message_except = "Erro ao cadastrar evento nos jogos "
    for item in df.iterrows():
        if not event_not_exist(item[1]["Event"]):
            if not game_not_exist(item[1]["Year"], item[1]["Season"], item[1]["City"]):
                if game_event_not_exist(item[1]["Year"], item[1]["Season"], item[1]["City"], item[1]["Event"]):
                    try:
                        register_game_event(item[1]["Year"], item[1]["Season"], item[1]["City"], item[1]["Event"])
                    except:
                        register_message(item[1]["Event"], message_except, request)

def game_event_not_exist(year, season, city, event):
    return GameEvents.objects.filter(
        game=get_game_by_data(year, season, city),
        event=get_event_by_name(event)
    ).first() == None

def get_game_event_not_exist(year, season, city, event):
    return GameEvents.objects.get(
        game=get_game_by_data(year, season, city),
        event=get_event_by_name(event)
    )

def register_game_event(year, season, city, event):
    GameEvents.objects.create(
        game=get_game_by_data(year, season, city),
        event=get_event_by_name(event)
    )

def save_athlete(athlete, request):
    df = athlete.drop_duplicates("ID", keep='first')
    df[['Name', 'Sex']].fillna(value=" ", inplace=True)
    df['Height'].fillna(value=df['Height'].mean(), inplace=True)
    df['Weight'].fillna(value=df['Weight'].mean(), inplace=True)

    message_except = "Erro ao cadastrar o atleta "
    for item in df.iterrows():
        if not region_not_exist(item[1]["NOC"]):
            if not sport_not_exist(item[1]["Sport"]):
                if athlete_not_exist(item[1]["Name"],item[1]["Sex"],
                                     item[1]["Height"],item[1]["Weight"],
                                     item[1]["NOC"], item[1]["Sport"]):
                    try:
                        register_atlete(item[1]["Name"],item[1]["Sex"],item[1]["Height"],
                                        item[1]["Weight"],item[1]["NOC"], item[1]["Sport"])
                    except:
                        register_message(item[1]["ID"]+" "+item[1]["Name"], message_except, request)

def athlete_not_exist(name, sex, height, weight, noc, sport):
    return Athlete.objects.filter(
        name= name,
        sex=sex,
        height= height,
        weight= weight,
        team= get_region_by_noc(noc),
        sport= get_sport_by_name(sport)
    ).first() == None

def get_athlete(name, sex, height, weight, noc, sport):
    return Athlete.objects.get(
        name= name,
        sex=sex,
        height= height,
        weight= weight,
        team= get_region_by_noc(noc),
        sport= get_sport_by_name(sport)
    )

def register_atlete(name, sex, height, weight, noc, sport):
    Athlete.objects.create(
        name= name,
        sex=sex,
        height= height,
        weight= weight,
        team= get_region_by_noc(noc),
        sport= get_sport_by_name(sport)
    )

def save_event_participants(athlete, request):
    athlete[['Name', 'Sex', 'Medal']].fillna(value="", inplace=True)
    athlete['Height'].fillna(value=athlete['Height'].mean(), inplace=True)
    athlete['Weight'].fillna(value=athlete['Weight'].mean(), inplace=True)
    athlete['Age'].fillna(value=athlete['Age'].mean(), inplace=True)
    athlete.sort_values("Name", inplace=True)

    message_except = "Erro ao cadastrar o atleta no evento"
    for item in athlete.iterrows():
        if not region_not_exist(item[1]["NOC"]):
            if not sport_not_exist(item[1]["Sport"]):
                if not game_event_not_exist(item[1]["Year"], item[1]["Season"], item[1]["City"], item[1]["Event"]):
                    if not athlete_not_exist(item[1]["Name"], item[1]["Sex"], item[1]["Height"], item[1]["Weight"],  item[1]["NOC"], item[1]["Sport"]):
                        if event_participant_not_exist(item[1]["Name"], item[1]["Sex"], item[1]["Height"], item[1]["Weight"], item[1]["Age"],  item[1]["NOC"], item[1]["Sport"], item[1]["Year"], item[1]["Season"], item[1]["City"], item[1]["Event"]):
                            try:
                                register_event_participants(item[1]["Name"], item[1]["Sex"], item[1]["Height"], item[1]["Weight"], item[1]["Age"],
                                                item[1]["NOC"], item[1]["Sport"], item[1]["Year"], item[1]["Season"],
                                                item[1]["City"], item[1]["Event"], item[1]["Medal"])
                            except:
                                register_message(item[1]["Name"]+" "+item[1]["Event"], message_except, request)

def event_participant_not_exist(name, sex, height, weight, age,  noc, sport, year, season, city, event):
    return EventParticipant.objects.filter(
        age=age,
        game_event=get_game_event_not_exist(year, season, city, event),
        athlete=get_athlete(name, sex, height, weight, noc, sport)
    ).first() == None

def register_event_participants(name, sex, height, weight, age, noc, sport, year, season, city, event, medal):
    EventParticipant.objects.create(
        age= age,
        game_event=get_game_event_not_exist(year, season, city, event),
        athlete=get_athlete(name, sex, height, weight, noc, sport),
        medal=get_medal(medal)
    )

def get_medal(medal):
    return Medal.objects.get(
        name= medal
    )