from core import models

def list_all():
    return models.Event.objects.all().order_by('name')


def get_by_id(event_id):
    try:
        return models.Event.objects.get(id=event_id)
    except:
        return None