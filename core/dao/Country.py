from core import models

def list_all():
    return list(models.Country.objects.all().order_by('noc'))

def get_by_id(id):
    try:
        return models.Country.objects.get(id=id)
    except:
        None

def get_region_by_noc(noc):
    try:
        return models.Country.objects.get(noc=noc)
    except:
        return None

def get_region_by_name(name):
    try:
        return models.Country.objects.get(name=name)
    except:
        return None

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

def filter_region_by_note(notes):
    try:
        return models.Country.objects.filter(notes=notes)
    except:
        return []

def filter(noc, name, notes):
    list_noc = []
    list_name = []
    list_note = []

    if noc != "":
        list_noc = list(filter_region_by_noc(noc))

    if name != "":
        list_name = list(filter_region_by_name(name))

    if notes != "":
        list_note = list(filter_region_by_note(notes))

    return intersection(list_noc, list_name, list_note)

def intersection(noc, name, notes):
    response = intersection_execute(noc, name)
    response = intersection_execute(response, notes)

    return response

def intersection_execute(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1

    return [value for value in list1 if value in list2]

def create(noc, name, notes):
    return models.Country.objects.create(
        noc=noc,
        name=name,
        notes=notes
    )

def delete(id):
    try:
        country = models.Country.objects.get(id=id)
        if country:
            country.delete()
            return True
    except:
        return False


def update(id, noc, name, notes):
    try:
        return models.Country.objects.filter(id=id).update(
            noc=noc,
            name=name,
            notes=notes
        )
    except:
        return None