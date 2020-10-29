from core import models
import pandas as pd

def list_all():
    return models.City.objects.all().order_by('name')

def get_registered_city():
    city = models.City.objects.all()
    return pd.DataFrame(list(city.values()))

def get_city_by_name(city):
    try:
        return models.City.objects.get(name=city)
    except:
        None

def create(city):
    return models.City.objects.create(
        name=city
    )