from django.test import TestCase
import pandas as pd

from core.controllers.upload import views as upload
from core.models import *

class uploadTests(TestCase):
    def setUp(self):
        Country.objects.create(
            noc="AFG",
            name="Afghanistan",
            notes=""
        )

    def test_upload_create_region(self):
        df = pd.DataFrame([["BRA", "Brazil", ""]], [0], ["NOC", "region", "notes"])
        upload.register_country(df)

    def test_upload_get_region_by_noc_ok(self):
        region = upload.get_region_by_noc("AFG")
        self.assertEqual(region.name, "Afghanistan")

