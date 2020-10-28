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

    def test_template_athlete_view_status_ok(self):
        response = self.client.get(reverse("athlete_view"))
        self.assertEqual(response.status_code, 200)

    def test_template_athlete_view(self):
        response = self.client.get(reverse("athlete_view"))
        self.assertTemplateUsed(response, "athlete/view.html")

    def test_template_athlete_view_not_exists(self):
        response = self.client.get(reverse("home_view"))
        self.assertTemplateNotUsed(response, "athlete/view.html")