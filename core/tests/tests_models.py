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

    def test_upload_create_region(self):
        df = pd.DataFrame([["BRA", "Brazil", ""]], [0], ["NOC", "region", "notes"])
        country = upload.register_country(df)
        self.assertEqual(country.name, "Brazil")

    def test_upload_get_region_by_noc(self):
        region = upload.get_region_by_noc("AFG")
        self.assertEqual(region.name, "Afghanistan")

    def test_upload_create_sport(self):
        sport = upload.register_sport("Judo")
        self.assertEqual(sport.name, "Judo")

    def test_upload_get_sport_by_name(self):
        sport = upload.get_sport_by_name("Basketball")
        self.assertEqual(sport.name, "Basketball")

    def test_upload_get_event_by_id(self):
        event = upload.get_event_by_id(1)
        self.assertEqual(event.name, "Basketball Men's Basketball")

    def test_upload_get_event_by_name(self):
        event = upload.get_event_by_name("Basketball Men's Basketball")
        self.assertEqual(event.id, 1)

    def test_upload_create_event(self):
        event = upload.register_event("Basketball Women's Basketball", "Basketball")
        self.assertEqual(event.name, "Basketball Women's Basketball")
