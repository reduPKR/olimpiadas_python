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
    path('athlete/create/', page.create_athlete, name="create_athlete_view"),
    path('athlete/update/<int:id>', page.update_athlete, name="create_athlete_view"),
    path('athlete/participation/<int:id>', page.add_participation, name="participation_athlete_view"),
    path('region/list/', page.region_list, name="list_region_view"),
    path('region/filter/', page.region_filter, name="filter_region_view"),
    path('region/view/', page.region_view, name="region_view"),
    path('region/create/', page.create_region, name="create_region_view"),

    path('upload/submit', upload.upload),
    path('athlete/filter/submit', page.athlete_filter_submit),
    path('athlete/delete/<int:id>/', page.athlete_delete),
    path('athlete/create/submit', page.create_athlete_submit),
    path('athlete/update/submit', page.update_athlete_submit),
    path('athlete/participation/submit', page.participation_athlete_submit),
    path('athlete/<int:athlete>/participation/delete/<int:id>/', page.participation_delete),
    path('region/filter/submit', page.region_filter_submit),
    path('region/create/submit', page.create_region_submit),
]
