from django.db import models



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    members = models.JSONField(default=list)

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    performed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} ({self.duration_minutes} min)"


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    score = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user}: {self.score}"
