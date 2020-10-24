from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from core.controllers.pages import views as page

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', RedirectView.as_view(url='/home/')),
    path('home/', page.home),
    path('upload/', page.upload),

    
]
