from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.IntegerField()
    height = models.IntegerField()
    gain_lose_maintain = models.IntegerField()
    cell = models.CharField(max_length=12,default='')
    breakTime = models.TimeField(blank=True,null=True)
    lunchTime = models.TimeField(blank=True,null=True)
    dinnerTime = models.TimeField(blank=True,null=True)
    
class Meal(models.Model):
    discoveryId = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    
class Pref_Dict(models.Model):
    name = models.CharField(max_length=32)
    
class Preference(models.Model):
    prefDictId = models.ForeignKey(Pref_Dict, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    
class User_Meal(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    mealId = models.ForeignKey(Meal, on_delete=models.CASCADE)
    date = models.DateField()
    break_lunch_dinner = models.IntegerField()
    
class User_Preference(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    preferenceId = models.ForeignKey(Preference, on_delete=models.CASCADE)
    like_neutral_dislike = models.IntegerField()

