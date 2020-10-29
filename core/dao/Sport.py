from core import models

def list_all():
    return models.Sport.objects.all().order_by('name')


def get_by_id(id):
    try:
        return models.Sport.objects.get(id=id)
    except:
        return None