# -*- coding: utf-8 -*-
from django.db import models
from .models import User_Preference

def getPrefDict(username):
    queryString = '''SELECT *
                     FROM app_user_preference up
                     INNER JOIN auth_user u on up.userId_id == u.id
                     INNER JOIN app_preference p on up.preferenceId_id == p.id
                     WHERE u.username == ''' + str(username)
    res = User_Preference.objects.raw(queryString)
    return res

def getTexts():
    queryString = '''    
    '''