from multiprocessing.sharedctypes import Value
from django.db import models
from datetime import datetime
from django.utils import timezone
class lang(models.Model):
    lang=models.CharField(max_length=150)
    user=models.CharField(max_length=150,default='arabic')
class adnan_test11(models.Model):
    noun = models.CharField(max_length=150)
    gnoun = models.CharField(max_length=150)
    animalNoun=models.CharField(max_length=150)
    plants=models.CharField(max_length=150)
    countries=models.CharField(max_length=150)
    inanimate=models.CharField(max_length=150)
    sum=models.CharField(max_length=150)
    user = models.CharField(max_length=150)
    letter = models.CharField(max_length=150 , default='أ',null=True,blank=True)
    room = models.CharField(max_length=150)
    def __str__(self):
        return self.room



class summeryOfLetter(models.Model):
    all_letter_as = models.CharField(max_length=2000000)
    room = models.CharField(max_length=150)
    time = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.room
class array(models.Model):
    status=models.CharField(max_length=1000,default='first',null=True,blank=True)
    room = models.CharField(max_length=150)
class players(models.Model):
    players= models.CharField(max_length=900000,null=True,blank=True)
    room = models.CharField(max_length=150)

class room_created(models.Model):
    user = models.CharField(max_length=100)
    room_created = models.CharField(max_length=10,null=True,blank=True)
    players=models.CharField(max_length=1000,null=True,blank=True)
    table=models.TextField(max_length=10000000000000000000,default='')
    def __str__(self):
         return self.table
