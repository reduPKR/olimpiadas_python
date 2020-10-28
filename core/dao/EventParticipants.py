from core import models

def filter(medals):
    participants = models.EventParticipant.objects.filter(medal__in=medals)

    if len(participants) > 0:
        return list(participants)
    return None

def filter_get_athlete(medals):
    participants = models.EventParticipant.objects.filter(medal__in=medals)

    athletes = []
    if len(participants) > 0:
        for item in participants:
            athletes.append(item.athlete)

    return athletes