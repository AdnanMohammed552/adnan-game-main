from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

class MyModel(models.Model):
    data = ArrayField(models.CharField(max_length=1000000000), blank=True)
    code = models.IntegerField(max_length=100,unique=True)
    delete = models.BooleanField(default=False)
    def __str__(self):
        return str(self.code)

class title(models.Model):
    user =models.CharField(max_length=100,null=True)
    title = models.CharField(max_length=200)
    code = models.IntegerField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    num = models.CharField(max_length=200,default='')
    delete = models.BooleanField(default=False)
    def __str__(self):
        return str(self.title)
class priv(models.Model):
    private = models.BooleanField(default=True)
    code = models.IntegerField(max_length=100,unique=True)
    def __str__(self):
        return str(self.code)

class room_created(models.Model):
    user = models.CharField(max_length=100)
    room_created = models.CharField(max_length=10,null=True,blank=True)
    players=models.CharField(max_length=1000,null=True,blank=True)
    table=models.TextField(max_length=10000000000000000000,default='')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return str(self.players)

class password(models.Model):
    code =models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=200)
    def __str__(self):
        return str(self.code)

class enumeration(models.Model):
    quiz_number = models.CharField(max_length=10,null=True,blank=True)
    user= models.CharField(max_length=10,unique=True)
    def __str__(self):
        return str(self.user)
class total_score(models.Model):
    total_score = models.CharField(max_length=1000000)
    user= models.CharField(max_length=10,unique=True)
    code =models.CharField(max_length=100,default='')
    def __str__(self):
        return str(self.user)

class enumeration_played(models.Model):
    quiz_number_played = models.CharField(max_length=10,null=True,blank=True)
    user= models.CharField(max_length=10,unique=True)
    def __str__(self):
        return str(self.user)
class played_quiz(models.Model):
    user= models.CharField(max_length=100)
    code= models.IntegerField(max_length=1000)
    name = models.CharField(max_length=200,default='')
    ids = models.BigIntegerField(default=0)
    def __str__(self):
        return str(self.code)
    class Meta:
        unique_together = ('code', 'user')

class image(models.Model):
    image = models.ImageField(upload_to='images/',default='images/3906412_DzsLBsC.png')
    user= models.CharField(max_length=100,null=True,blank=True)