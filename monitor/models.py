from __future__ import unicode_literals
from django.db import models

from django.utils import timezone

# Create your models here (basically database tables).

class Computer(models.Model):
    computer_name = models.CharField(max_length=100, primary_key=True)
    ip = models.CharField(max_length=25)
    activity = models.DateTimeField('latest activity')
    
    def __str__(self):
        return self.computer_name
    
    def isAlive(self):
        return (timezone.now() - self.activity < timezone.timedelta(minutes=10))

#class Activity(models.Model):
    #computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    #activity = models.DateTimeField('accessed jefit')
    
    #def __str__(self):
        #return str(self.activity)
    
    #def isAlive(self):
        #return self.activity >= timezone.now() - datetime.timedelta(minutes=5)