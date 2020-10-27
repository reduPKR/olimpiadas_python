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

        Sport.objects.create(
            name="Basketball"
        )

    def test_upload_create_region(self):
        df = pd.DataFrame([["BRA", "Brazil", ""]], [0], ["NOC", "region", "notes"])
        upload.register_country(df)

    def test_upload_get_region_by_noc(self):
        region = upload.get_region_by_noc("AFG")
        self.assertEqual(region.name, "Afghanistan")

    def test_upload_create_sport(self):
        upload.register_sport("Judo")

    def test_upload_get_sport_byname(self):
        sport = upload.get_sport_by_name("Basketball")
        self.assertEqual(sport.name, "Basketball")

