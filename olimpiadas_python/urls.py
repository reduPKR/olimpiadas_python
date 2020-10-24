from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from core.controllers.home import views as home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', RedirectView.as_view(url='/home/')),
    path('home/', home.menu_home),
]
