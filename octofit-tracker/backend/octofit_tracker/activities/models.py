from django.db import models


class Activity(models.Model):
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    performed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} ({self.duration_minutes} min)"
