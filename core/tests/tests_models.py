from django.test import TestCase
import pandas as pd

import core.dao as dao
from core.models import *

class uploadTests(TestCase):
    #Aqui vou testar apenas metodos que acessaram DB durante upload
    def setUp(self):
        country = Country.objects.create(
            noc="CHN",
            name="China",
            notes=""
        )

        sport = Sport.objects.create(
            name="Basketball"
        )

        event = Event.objects.create(
            name="Basketball Men's Basketball",
            sport=sport
        )

        city = City.objects.create(
            name= "Barcelona"
        )

        season = Season.objects.create(
            name= "Summer"
        )

        game = Game.objects.create(
            year=1992,
            season=season,
            city=city
        )

        game_event = GameEvents.objects.create(
            game=game,
            event=event
        )

        athlete = Athlete.objects.create(
            name= "A Dijiang",
            sex="M",
            height= 180,
            weight= 80,
            team= country,
            sport= sport
        )

        Medal.objects.create(
            name="Gold"
        )

    def test_upload_create_region(self):
        country = dao.Country.create("BRA", "Brazil", "")
        self.assertEqual(country.id, 2)

    def test_upload_get_region_by_noc(self):
        region = dao.Country.get_region_by_noc("CHN")
        self.assertEqual(region.name, "China")

    def test_upload_create_sport(self):
        sport = dao.Sport.create("Judo")
        self.assertEqual(sport.name, "Judo")

    def test_upload_get_sport_by_name(self):
        sport = dao.Sport.get_sport_by_name("Basketball")
        self.assertEqual(sport.id, 1)

    def test_upload_get_event_by_id(self):
        event = dao.Event.get_event_by_id(1)
        self.assertEqual(event.name, "Basketball Men's Basketball")

    def test_upload_get_event_by_name(self):
        event = dao.Event.get_event_by_name("Basketball Men's Basketball")
        self.assertEqual(event.id, 1)

    def test_upload_create_event(self):
        sport = dao.Sport.get_sport_by_name("Basketball")
        event = dao.Event.create("Basketball Women's Basketball", sport)
        self.assertEqual(event.id, 2)

    def test_upload_get_city_by_name(self):
        city = dao.City.get_city_by_name("Barcelona")
        self.assertEqual(city.id, 1)

    def test_upload_create_city(self):
        city = dao.City.create("London")
        self.assertEqual(city.id, 2)

    def test_upload_get_season_by_name(self):
        season = dao.Season.get_season_by_name("Summer")
        self.assertEqual(season.id, 1)

    def test_upload_create_season(self):
        season = dao.Season.create("Winter")
        self.assertEqual(season.id, 2)

    def test_upload_get_game_by_id(self):
        game = dao.Game.get_game_by_id(1)
        result = "{} {}".format(game.year, game.season.name)
        self.assertEqual(result, "1992 Summer")

    def test_upload_create_game(self):
        season = dao.Season.get_season_by_name("Summer")
        city = dao.City.get_city_by_name("Barcelona")
        game = dao.Game.create(1993, season, city)
        self.assertEqual(game.id, 2)

    def test_upload_get_game_event_by_id(self):
        game_event = dao.GameEvent.get_game_event_by_id(1)
        game_name = "{} {}".format(game_event.game.year, game_event.game.season.name)
        result = "{}: {}".format(game_name, game_event.event.name)
        self.assertEqual(result, "1992 Summer: Basketball Men's Basketball")

    def test_upload_create_game_event(self):
        #ja esta cadastrado esse game evento
        game = dao.Game.get_game_by_id(1)
        event = dao.Event.get_by_id(1)
        game_event = dao.GameEvent.create(game,event)
        self.assertEqual(game_event.id, 2)

    def test_upload_get_athlete_by_id(self):
        athlete = dao.Athlete.get_by_id(1)
        self.assertEqual(athlete.name, "A Dijiang")

    def test_upload_create_athlete(self):
        athlete = dao.Athlete.create("Rafael Eduardo", 172,70,"M", 1, 1)
        self.assertEqual(athlete.id, 2)

    def test_upload_create_event_participants(self):
        athlete = dao.Athlete.get_by_id(1)
        game_event = dao.GameEvent.get_by_id(1)
        medal = dao.Medal.get_medal("Gold")
        participant = dao.EventParticipants.create(athlete, 24, game_event, medal)
        self.assertEqual(participant.id, 1)

    # ------------------------------------------------------------------------------------------------

    def test_athlete_list(self):
        lista = dao.Athlete.list_all()
        self.assertNotEqual(len(lista), 0)

    def test_athlete_get_by_id(self):
        athlete = dao.Athlete.get_by_id(1)
        self.assertEqual(athlete.name, "A Dijiang")

    def test_athlete_all_info_get_by_id(self):
        athlete = dao.Athlete.get_all_info_by_id(1)
        self.assertEqual(athlete.name, "A Dijiang")

    def test_athlete_delete_by_id(self):
        athlete = dao.Athlete.delete(1)
        self.assertTrue(athlete)
        
    # ------------------------------------------------------------------------------------------------

    def test_team_list(self):
        lista = dao.Country.list_all()
        self.assertNotEqual(len(lista), 0)

    # ------------------------------------------------------------------------------------------------

    def test_game_list(self):
        lista = dao.Game.list_all()
        self.assertNotEqual(len(lista), 0)

    # ------------------------------------------------------------------------------------------------

    def test_event_list(self):
        lista = dao.Event.list_all()
        self.assertNotEqual(len(lista), 0)

    # ------------------------------------------------------------------------------------------------
    def test_sport_list(self):
        lista = dao.Sport.list_all()
        self.assertNotEqual(len(lista), 0)

    # ------------------------------------------------------------------------------------------------
    def test_city_list(self):
        lista = dao.City.list_all()
        self.assertNotEqual(len(lista), 0)