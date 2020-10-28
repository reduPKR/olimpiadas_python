from core import models

def list_all():
    return models.Season.objects.all().order_by('name')