from core import models

def list_all():
    return models.Country.objects.all().order_by('noc')