from django.db import models

class Movie(models.Model):
    STATUSES = {
        "to_watch": "To watch",
        "watched": "Watched"
    }

    title = models.CharField()
    status = models.CharField(choices=STATUSES, default="to_watch")

