from django.db import models
from django.contrib.postgres.fields import ArrayField

class MyModel(models.Model):
    data = ArrayField(models.CharField(max_length=100), blank=True)
    code = models.IntegerField(max_length=100)