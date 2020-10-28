from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from core.controllers.pages import views as page
from core.controllers.upload import views as upload

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', RedirectView.as_view(url='/home/')),
    path('home/', page.home, name="home_view"),
    path('upload/', page.upload, name="upload_view"),
    path('athlete/list/', page.athlete_list, name="list_athlete_view"),
    path('athlete/filter/', page.athlete_filter, name="filter_athlete_view"),
    path('athlete/view/', page.athlete_view, name="athlete_view"),

    path('upload/submit', upload.upload),
    path('athlete/filter/submit', page.athlete_filter_submit),
    path('athlete/delete/<int:id>/', page.athlete_delete),
]
