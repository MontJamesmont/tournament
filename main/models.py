from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=32)

class User(models.Model):
    login = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    team_id = models.ForeignKey(Team, null=True)

class Category(models.Model):
    name=models.CharField(max_length=50)

class Coach(models.Model):
    user_id = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    team_id = models.ForeignKey(Team)
    
class Player(models.Model):
    user_id = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    team_id = models.ForeignKey(Team)
    
class Manager(models.Model):
    user_id = models.ForeignKey(User)


class Tournament(models.Model):
    name = models.CharField(max_length=50)
    start = models.DateField()
    end = models.DateField()
    manager = models.ForeignKey(Manager, null=True)
    coaches = models.ManyToManyField(Coach, verbose_name="lista trenerow", blank=True)
    players = models.ManyToManyField(Player, verbose_name="lista graczy", blank=True)
    categories = models.ManyToManyField(Category, verbose_name="lista kategorii", blank=True)
