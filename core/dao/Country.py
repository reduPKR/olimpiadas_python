from core import models

def list_all():
    return list(models.Country.objects.all().order_by('noc'))


def get_by_id(id):
    try:
        return models.Country.objects.get(id=id)
    except:
        None

def filter_region_by_noc(noc):
    try:
        return models.Country.objects.filter(noc=noc)
    except:
        return []

def filter_region_by_name(name):
    try:
        return models.Country.objects.filter(name=name)
    except:
        return []

def filter_region_by_note(note):
    try:
        return models.Country.objects.filter(note=note)
    except:
        return []

def filter(noc, name, note):
    list_noc = []
    list_name = []
    list_note = []

    if noc != "":
        list_noc = list(filter_region_by_noc(noc))

    if name != "":
        list_name = list(filter_region_by_name(name))

    if note != "":
        list_note = list(filter_region_by_note(note))

    return intersection(list_noc, list_name, list_note)

def intersection(noc, name, note):
    response = intersection_execute(noc, name)
    response = intersection_execute(response, note)

    return response

def intersection_execute(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1

    return [value for value in list1 if value in list2]