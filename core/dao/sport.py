from core import models

def list_all():
    return models.Sport.objects.all().order_by('name')