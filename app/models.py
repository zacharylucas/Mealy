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
    prefDict = models.CharField(max_length=2048,default='')
    mealDict = models.CharField(max_length=2048,default='')
    
class User_Meals(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    break_lunch_dinner = models.IntegerField()
    discoveryId = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
