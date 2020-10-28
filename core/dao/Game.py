from core import models

def list_all():
    return models.Game.objects.all().order_by('year')