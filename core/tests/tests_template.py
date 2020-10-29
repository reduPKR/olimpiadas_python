from django.test import TestCase
from django.urls import reverse

class TemplatesViewTests(TestCase):

    #------------------------------------------------------------------------------------------------#
    def test_template_home_status_ok(self):
        response = self.client.get(reverse("home_view"))
        self.assertEqual(response.status_code, 200)

    def test_template_home(self):
        response = self.client.get(reverse("home_view"))
        self.assertTemplateUsed(response, "menu/home.html")

    def test_template_home_not_exists(self):
        response = self.client.get(reverse("upload_view"))
        self.assertTemplateNotUsed(response, "menu/home.html")

    #------------------------------------------------------------------------------------------------#

    def test_template_upload_status_ok(self):
        response = self.client.get(reverse("upload_view"))
        self.assertEqual(response.status_code, 200)

    def test_template_upload(self):
        response = self.client.get(reverse("upload_view"))
        self.assertTemplateUsed(response, "upload/upload.html")

    def test_template_upload_not_exists(self):
        response = self.client.get(reverse("home_view"))
        self.assertTemplateNotUsed(response, "upload/upload.html")

    # ------------------------------------------------------------------------------------------------#

    def test_template_list_athlete_status_ok(self):
        response = self.client.get(reverse("list_athlete_view"))
        self.assertEqual(response.status_code, 200)

    def test_template_list_athlete(self):
        response = self.client.get(reverse("list_athlete_view"))
        self.assertTemplateUsed(response, "athlete/list.html")

    def test_template_list_athlete_not_exists(self):
        response = self.client.get(reverse("home_view"))
        self.assertTemplateNotUsed(response, "athlete/list.html")

    # ------------------------------------------------------------------------------------------------#

    def test_template_filter_athlete_status_ok(self):
        response = self.client.get(reverse("filter_athlete_view"))
        self.assertEqual(response.status_code, 200)

    def test_template_filter_athlete(self):
        response = self.client.get(reverse("filter_athlete_view"))
        self.assertTemplateUsed(response, "athlete/filter.html")

    def test_template_filter_athlete_not_exists(self):
        response = self.client.get(reverse("home_view"))
        self.assertTemplateNotUsed(response, "athlete/filter.html")

    # --------------------------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------------------------

    def test_template_athlete_create_status_ok(self):
        response = self.client.get(reverse("create_athlete_view"))
        self.assertEqual(response.status_code, 200)

    def test_template_athlete_create(self):
        response = self.client.get(reverse("create_athlete_view"))
        self.assertTemplateUsed(response, "athlete/create.html")

    def test_template_athlete_create_not_exists(self):
        response = self.client.get(reverse("home_view"))
        self.assertTemplateNotUsed(response, "athlete/create.html")

    # --------------------------------------------------------------------------------------------------

    def test_template_athlete_update_status_ok(self):
        response = self.client.get(reverse("create_athlete_view"))
        self.assertEqual(response.status_code, 200)

    def test_template_athlete_update(self):
        response = self.client.get(reverse("create_athlete_view"))
        self.assertTemplateUsed(response, "athlete/create.html")

    def test_template_athlete_update_not_exists(self):
        response = self.client.get(reverse("home_view"))
        self.assertTemplateNotUsed(response, "athlete/create.html")

    # --------------------------------------------------------------------------------------------------

    def test_template_regions_list_status_ok(self):
        response = self.client.get(reverse("list_region_view"))
        self.assertEqual(response.status_code, 200)

    def test_template_regions_list(self):
        response = self.client.get(reverse("list_region_view"))
        self.assertTemplateUsed(response, "region/list.html")

    def test_template_regions_list_not_exists(self):
        response = self.client.get(reverse("home_view"))
        self.assertTemplateNotUsed(response, "region/list.html")

    # --------------------------------------------------------------------------------------------------

    def test_template_regions_filter_status_ok(self):
        response = self.client.get(reverse("filter_region_view"))
        self.assertEqual(response.status_code, 200)

    def test_template_regions_filter(self):
        response = self.client.get(reverse("filter_region_view"))
        self.assertTemplateUsed(response, "region/filter.html")

    def test_template_regions_filter_not_exists(self):
        response = self.client.get(reverse("home_view"))
        self.assertTemplateNotUsed(response, "region/filter.html")