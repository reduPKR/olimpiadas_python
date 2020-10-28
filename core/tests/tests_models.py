from django.test import TestCase
import pandas as pd

from core.controllers.upload import views as upload
from core.dao import athlete
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
        df = pd.DataFrame([["BRA", "Brazil", ""]], [0], ["NOC", "region", "notes"])
        country = upload.register_country(df)
        self.assertEqual(country.id, 2)

    def test_upload_get_region_by_noc(self):
        region = upload.get_region_by_noc("CHN")
        self.assertEqual(region.name, "China")

    def test_upload_create_sport(self):
        sport = upload.register_sport("Judo")
        self.assertEqual(sport.name, "Judo")

    def test_upload_get_sport_by_name(self):
        sport = upload.get_sport_by_name("Basketball")
        self.assertEqual(sport.id, 1)

    def test_upload_get_event_by_id(self):
        event = upload.get_event_by_id(1)
        self.assertEqual(event.name, "Basketball Men's Basketball")

    def test_upload_get_event_by_name(self):
        event = upload.get_event_by_name("Basketball Men's Basketball")
        self.assertEqual(event.id, 1)

    def test_upload_create_event(self):
        event = upload.register_event("Basketball Women's Basketball", "Basketball")
        self.assertEqual(event.id, 2)

    def test_upload_get_city_by_name(self):
        city = upload.get_city_by_name("Barcelona")
        self.assertEqual(city.id, 1)

    def test_upload_create_city(self):
        city = upload.register_city("London")
        self.assertEqual(city.id, 2)

    def test_upload_get_season_by_name(self):
        season = upload.get_season_by_name("Summer")
        self.assertEqual(season.id, 1)

    def test_upload_create_season(self):
        season = upload.register_season("Winter")
        self.assertEqual(season.id, 2)

    def test_upload_get_game_by_id(self):
        game = upload.get_game_by_id(1)
        result = "{} {}".format(game.year, game.season.name)
        self.assertEqual(result, "1992 Summer")

    def test_upload_create_game(self):
        game = upload.register_game(1993, "Summer", "Barcelona")
        self.assertEqual(game.id, 2)

    def test_upload_get_game_event_by_id(self):
        game_event = upload.get_game_event_by_id(1)
        game_name = "{} {}".format(game_event.game.year, game_event.game.season.name)
        result = "{}: {}".format(game_name, game_event.event.name)
        self.assertEqual(result, "1992 Summer: Basketball Men's Basketball")

    def test_upload_create_game_event(self):
        #ja esta cadastrado esse game evento
        game_event = upload.register_game_event(1,1)
        self.assertEqual(game_event.id, 2)

    def test_upload_get_athlete_by_id(self):
        athlete = upload.get_athlete_by_id(1)
        self.assertEqual(athlete.name, "A Dijiang")

    def test_upload_create_athlete(self):
        athlete = upload.register_atlete("Rafael Eduardo", "M",172,70,"CHN", "Basketball")
        self.assertEqual(athlete.id, 2)

    def test_upload_create_event_participants(self):
        participant = upload.register_event_participants(1, 24,1,"Gold")
        self.assertEqual(participant.id, 1)

    # ------------------------------------------------------------------------------------------------

    def test_athlete_list(self):
        athletes = athlete.list_all()
        self.assertNotEqual(len(athletes), 0)