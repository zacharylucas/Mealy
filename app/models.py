from django.db import models
from django.contrib.auth.models import User
import json

class UserInfo(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    gain_lose_maintain = models.IntegerField(default=3)
    cell = models.CharField(max_length=12,default='')
    breakTime = models.TimeField(blank=True,null=True)
    lunchTime = models.TimeField(blank=True,null=True)
    dinnerTime = models.TimeField(blank=True,null=True)
    dietRestrict = models.CharField(max_length=100,default='')
    allergies = models.CharField(max_length=100,default='')
    prefDict = models.CharField(max_length=2048,default='')
    mealDict = models.CharField(max_length=2048,default='')
    
def getPrefDict(uid):
    u = UserInfo(userId=uid)
    return json.load(u.prefDict)

def updatePrefDict(uid, newPrefDict):
    u = u = UserInfo(userId=uid)
    s = json.dumps(newPrefDict)
    u.prefDict = s
    u.save()
    
def getMealDict(uid):
    u = UserInfo(userId=uid)
    return json.load(u.mealDict)

def updateMealDict(uid, newMealDict):
    u = UserInfo(userId=uid)
    s = json.dumps(newMealDict)
    u.mealDict = s
    u.save()
    
def createUserInfo(uid):
    ui = UserInfo(userId=uid)
    ui.save();
    
def updateUserInfo(uid, w=0, h=0, glm=3, phone='', btime=None,
                   ltime=None, dtime=None, restrict='', allergy=''):
    u = UserInfo(userId=uid)
    u.weight = w
    u.height = h
    u.gain_lose_maintain = glm
    u.cell = phone
    u.breakTime = btime
    u.lunchTime = ltime
    u.dinnerTime = dtime
    u.dietRestrict = restrict
    u.allergies = allergy
    u.save()