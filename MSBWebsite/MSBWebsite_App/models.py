from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Statistics(models.Model):
    statistics_id = models.AutoField(primary_key=True)
    position = models.IntegerField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    
    burned_calories = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'statistics'


class Route(models.Model):
    route_id = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'route'


class Practice(models.Model):
    practice_id = models.AutoField(primary_key=True)
    route = models.ForeignKey(Route, models.DO_NOTHING)
    statistics = models.OneToOneField(Statistics, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'practice'
        

class Ranking(models.Model):
    ranking_id = models.AutoField(primary_key=True)
    user = models.ManyToManyField(User)

    class Meta:
        managed = True
        db_table = 'ranking'


class Race(models.Model):
    race_id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField()
    city = models.CharField(max_length=45, blank=True, null=True)
    limit_of_participants = models.IntegerField()
    name = models.CharField(max_length=45)
    route = models.ForeignKey(Route, models.DO_NOTHING)
    ranking = models.OneToOneField(Ranking, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'race'
    

class User(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    user_id = models.AutoField("user's identification",primary_key=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=True)
    password = models.CharField(max_length=20)
    height = models.IntegerField(blank=True, null=True)
    weigth = models.FloatField(blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    avatar = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45)
    second_name = models.CharField(db_column='second name', max_length=45)  # Field renamed to remove unsuitable characters.
    nick = models.CharField(max_length=45, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=3, blank=True, null=True)
    practice = models.ManyToManyField(Practice)
    friend = models.ManyToManyField("self", blank=True)
    route = models.ManyToManyField(Route, null = True)
    class Meta:
        managed = True
        db_table = 'user'