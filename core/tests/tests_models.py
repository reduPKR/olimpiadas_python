from django.test import TestCase
import pandas as pd

from core.controllers.upload import views as upload
from core.models import *

class uploadTests(TestCase):
    #Aqui vou testar apenas metodos que acessaram DB durante upload
    def setUp(self):
        Country.objects.create(
            noc="AFG",
            name="Afghanistan",
            notes=""
        )

        sport = Sport.objects.create(
            name="Basketball"
        )

        Event.objects.create(
            name="Basketball Men's Basketball",
            sport=sport
        )

        city = City.objects.create(
            name= "Barcelona"
        )

        season = Season.objects.create(
            name= "Summer"
        )

        Game.objects.create(
            year=1992,
            season=season,
            city=city
        )

    def test_upload_create_region(self):
        df = pd.DataFrame([["BRA", "Brazil", ""]], [0], ["NOC", "region", "notes"])
        country = upload.register_country(df)
        self.assertEqual(country.id, 2)

    def test_upload_get_region_by_noc(self):
        region = upload.get_region_by_noc("AFG")
        self.assertEqual(region.name, "Afghanistan")

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