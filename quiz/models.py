from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

class MyModel(models.Model):
    data = ArrayField(models.CharField(max_length=100), blank=True)
    code = models.IntegerField(max_length=100)

class title(models.Model):
    user =models.CharField(max_length=100,null=True)
    title = models.CharField(max_length=200)
    code = models.IntegerField(max_length=100)
    date = models.DateTimeField(default=timezone.now)


class room_created(models.Model):
    user = models.CharField(max_length=100)
    room_created = models.CharField(max_length=10,null=True,blank=True,unique=True)
    players=models.CharField(max_length=1000,null=True,blank=True)
    table=models.TextField(max_length=10000000000000000000,default='')
    date = models.DateTimeField(auto_now_add=True, blank=True)

