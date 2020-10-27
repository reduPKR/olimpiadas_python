from django.test import TestCase
from django.urls import reverse

from core.controllers.upload import views as upload

class uploadTests(TestCase):
    #Testes de acesso ao banco de dados no upload
    def upload_get_region_by_noc(self):
        region = upload.get_region_by_noc("AFG")
        self.assertEqual(region.name, "Afghanistan")

        region = upload.get_region_by_noc("BRA")
        self.assertEqual(region.name, "Brazil")

        region = upload.get_region_by_noc("HKG")
        self.assertEqual(region.name, "China")