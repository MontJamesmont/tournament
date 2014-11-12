from django.db import models

from main.models1 import *

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    KATA = 'KT'
    KUMITE = 'KM'
    TYPE_CHOICES = (
        (KATA, 'kata'),
        (KUMITE, 'kumite')
    )
    type = models.CharField(max_length=3,
                                      choices=TYPE_CHOICES,
                                      default=None)
    
    def __unicode__(self):
        return self.name
    
class Fight(models.Model):
    tournament_id = models.ForeignKey(Tournament)
    category_id = models.ForeignKey(Category)
    firstplayer = models.ForeignKey(Player)
    secondplayer = models.ForeignKey(Player)
    winner = models.IntegerField()
    TYPE_CHOICES = (
        ('knock', 'knockout'),
        ('walko', 'walkover'),
        ('arbit', 'arbiters'),
        ('wazar', 'wazari')
    )
    reason = models.CharField(max_length=5,
                                      choices=TYPE_CHOICES,
                                      default='arbiters')
    arbitersfor = models.IntegerField()
    arbitersagainst = models.IntegerField()
    arbitersdraw = models.IntegerField()
    round = models.IntegerField()
    