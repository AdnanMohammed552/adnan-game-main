from datetime import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class room_created(models.Model):
    user = models.CharField(max_length=100)
    room_created = models.CharField(max_length=10,null=True,blank=True,unique=True)
    players=models.CharField(max_length=1000,null=True,blank=True)
    table=models.TextField(max_length=10000000000000000000,default='')
    date = models.DateTimeField(auto_now_add=True, blank=True)



class played(models.Model):
    user= models.CharField(max_length=100)
    room_played = models.CharField(max_length=10,null=True,blank=True,unique=True)
