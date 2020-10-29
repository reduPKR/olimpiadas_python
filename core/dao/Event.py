from core import models
import pandas as pd

def list_all():
    return models.Event.objects.all().order_by('name')

def get_by_id(event_id):
    try:
        return models.Event.objects.get(id=event_id)
    except:
        return None

def get_registered_events():
    events = models.Event.objects.all()
    return pd.DataFrame(list(events.values()))

def get_event_by_id(event_id):
    try:
        return models.Event.objects.get(id=event_id)
    except:
        None

def get_event_by_name(event):
    try:
        return models.Event.objects.get(name=event)
    except:
        None

def create(event, sport):
    return Event.objects.create(
        name= event,
        sport= sport
    )