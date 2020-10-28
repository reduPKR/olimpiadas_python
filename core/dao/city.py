from core import models

def list_all():
    return models.City.objects.all().order_by('name')