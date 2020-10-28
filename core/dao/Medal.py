from core import models
from django.db.models import Q

def filter(gold, silver, bronze):
    medals = models.Medal.objects.filter(Q(name=gold) | Q(name=silver) | Q(name=bronze))

    if len(medals) > 0:
        return list(medals)
    return None

