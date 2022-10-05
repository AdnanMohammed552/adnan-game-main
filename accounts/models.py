from django.db import models
from django.contrib.auth.models import User


class room_created(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    room_created = models.CharField(max_length=10)