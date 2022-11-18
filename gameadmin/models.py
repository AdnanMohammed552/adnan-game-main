from django.db import models


class startingroom(models.Model):
    room = models.CharField(max_length=150)
    started = models.BooleanField()
    end = models.BooleanField()
    def __str__(self):
        return self.room

class room(models.Model):
    room = models.CharField(max_length=150)