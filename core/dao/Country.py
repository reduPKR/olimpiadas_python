from core import models

def list_all():
    return list(models.Country.objects.all().order_by('noc'))


def get_by_id(id):
    try:
        return models.Country.objects.get(id=id)
    except:
        None