# models.py
from djongo import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    # ... other fields ...

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ArrayField(model_container=User)
    # ... other fields ...

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    # ... other fields ...

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    # ... other fields ...

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # ... other fields ...
