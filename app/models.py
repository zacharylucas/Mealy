from django.db import models
from django.contrib.auth.models import User
import json

class UserInfo(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    gain_lose_maintain = models.IntegerField(default=3)
    cell = models.CharField(max_length=12,default='')
    breakTime = models.TimeField(blank=True,null=True)
    lunchTime = models.TimeField(blank=True,null=True)
    dinnerTime = models.TimeField(blank=True,null=True)
    dietRestrict = models.CharField(max_length=100,default='')
    allergies = models.CharField(max_length=100,default='')
    prefDict = models.TextField(default='')
    mealDict = models.TextField(default='')

def getPrefDict(uid):
    res = UserInfo.objects.raw('select * from app_userinfo ui where ui.userId_id == %s', [uid.id])[0]
    if str(res.prefDict) == '':
        return {}
    return json.loads(str(res.prefDict))

def updatePrefDict(uid, newPrefDict):
    u = UserInfo(userId=uid)
    s = json.dumps(newPrefDict)
    u.userId = uid
    u.prefDict = s
    u.save(force_update=True)

def getMealDict(uid):
    res = UserInfo.objects.raw('select * from app_userinfo ui where ui.userId_id == %s', [uid.id])[0]
    if str(res.mealDict) == '':
        return {}
    return json.loads(str(res.mealDict))

def updateMealDict(uid, newMealDict, newPrefDict):
    u = UserInfo(userId=uid)
    s = json.dumps(newMealDict)
    s2 = json.dumps(newPrefDict)
    u.userId = uid
    u.mealDict = s
    u.prefDict = s2
    u.save(force_update=True)

def createUserInfo(uid):
    ui = UserInfo(userId=uid)
    ui.save();

def updateUserInfo(uid, w=0, h=0, glm=3, phone='', btime=None,
                   ltime=None, dtime=None, restrict='', allergy=''):
    u = UserInfo(userId=uid)
    u.userId = uid
    u.weight = w
    u.height = h
    u.gain_lose_maintain = glm
    u.cell = phone
    u.breakTime = btime
    u.lunchTime = ltime
    u.dinnerTime = dtime
    u.dietRestrict = restrict
    u.allergies = allergy
    u.save(force_update=True)
