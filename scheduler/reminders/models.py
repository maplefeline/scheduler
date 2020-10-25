from django.db import models  # type: ignore


class Reminder(models.Model):
    date = models.DateTimeField("date")

    class Meta:
        ordering = ["date"]
