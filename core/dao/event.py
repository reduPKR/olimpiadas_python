from core import models

def list_all():
    return models.Event.objects.all().order_by('name')