from django.db import models
from django.utils import timezone


class startingroom(models.Model):
    room = models.CharField(max_length=150)
    started = models.BooleanField()
    end = models.BooleanField()
    time = models.DateTimeField(default=timezone.now)
    admin=models.CharField(max_length=150,default='a')

    def __str__(self):
        return self.room

class room(models.Model):
    room = models.CharField(max_length=150)

class x():
    pass