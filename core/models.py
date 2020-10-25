from django.db import models

class Country(models.Model):
    noc = models.CharField(max_length=3)
    name = models.CharField(max_length=60)
    notes = models.CharField(max_length=60)

    class Meta:
        db_table = 'country'

class City(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        db_table = 'city'

class Sport(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'sport'

class Athlete(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    sex = models.CharField(max_length=1)

    team = models.ForeignKey(Country, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    class Meta:
        db_table = 'athlete'

class Season(models.Model):
    name = models.CharField(max_length=6)

    class Meta:
        db_table = 'season'

class Game(models.Model):
    year = models.IntegerField()

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    class Meta:
        db_table = 'game'

class Event(models.Model):
    name = models.CharField(max_length=100)

    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    class Meta:
        db_table = 'event'

class Medal(models.Model):
    name = models.CharField(max_length=6)

    class Meta:
        db_table = 'medal'

class GameEvents(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        db_table = 'game_event'

class EventParticipant(models.Model):
    game_event = models.ForeignKey(GameEvents, on_delete=models.CASCADE)
    medal = models.ForeignKey(Medal, on_delete=models.CASCADE, null=True)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)

    class Meta:
        db_table = 'event_participants'