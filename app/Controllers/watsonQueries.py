import json
import sys
import os
from watson_developer_cloud import DiscoveryV1
import random

breakfast_discovery = DiscoveryV1(
    username = '443e6698-a0eb-4be8-87a6-dddf917f8e08',
    password = 'MRIonJJP5wHl',
    version = '2017-11-07'
)

lunch_discovery = DiscoveryV1(
    username = '2e414ebd-3356-4218-a8ff-1fa0e4976231',
    password = 'xiosMyPLM0jR',
    version = '2017-11-07'
)

dinner_discovery = DiscoveryV1(
    username = '7f31ee94-5960-4498-b9de-72fa3db9b234',
    password = 'ZH2Z1SNpWYD4',
    version = '2017-11-07'
)

breakfast_environment_id = '9eca8cd5-10d4-47f4-b2f0-6c5987717d48'
breakfast_collection_id = 'a1169358-2112-401e-b0a0-9e6cdccb5129'

lunch_environment_id = 'e8a03832-1ad4-4c57-a8a9-4d4b3ae99d6e'
lunch_collection_id = '11c9997b-bcd7-4d0f-97df-2b610ac9aebe'

dinner_environment_id = '6a487cbb-3a04-4f03-9f06-88084e3c2b6d'
dinner_collection_id = 'e32f6689-d733-42e2-814d-bf26b84d123d'

def queryWatson(queryString, count = ''):
    recipe_query = dinner_discovery.query(dinner_environment_id, dinner_collection_id, query= queryString, count = count)
    return recipe_query

def queryBreakfast(queryString, count = '7'):
    recipe_query = breakfast_discovery.query(breakfast_environment_id, breakfast_collection_id, query= queryString, count = count)
    return recipe_query

def queryLunch(queryString, count = '7'):
    recipe_query = lunch_discovery.query(lunch_environment_id, lunch_collection_id, query= queryString, count = count)
    return recipe_query

def queryDinner(queryString, count = '7'):
    recipe_query = dinner_discovery.query(dinner_environment_id, dinner_collection_id, query= queryString, count = count)
    return recipe_query

def makePlan(result1, result2):
    if(result1['matching_results'] == result2['matching_results']):
        plan = result1['results'][0:7]
    else:
        plan = [result1['results'][0],result2['results'][0],result1['results'][1], result2['results'][1],result1['results'][2],result2['results'][2], result1['results'][3]]
    return plan

def addCals(calRange):
    queryString = ''
    if calRange != [] and calRange[0] >= 0 and calRange[1] >= 0:
        queryString += r',calories>%d' % calRange[0]
        queryString += r',calories<%d' % calRange[1]
    return queryString

def breakfastPlan(prefDict,alleg,calRange):
    result1 = prefQueryBreakfastEgg(prefDict,alleg,calRange)
    result2 = prefQueryBreakfastSmooth(prefDict,alleg,calRange)
    if(result1['matching_results'] < 8):
        result1 = queryBreakfast('')
    if(result2['matching_results'] < 8):
        result2 = queryBreakfast('')

    return makePlan(result1,result2)

def lunchPlan(prefDict,alleg,calRange):
    result1 = prefQueryLunch(prefDict,alleg,calRange)
    result2 = prefQueryLunch(prefDict,alleg,calRange)
    if(result1['matching_results'] < 8):
        result1 = queryLunch('')
    if(result2['matching_results'] < 8):
        result2 = queryLunch('')

    return makePlan(result1,result2)

def dinnerPlan(prefDict,alleg,calRange):
    result1 = prefQueryDinner(prefDict,alleg,calRange)
    result2 = prefQueryDinner(prefDict,alleg,calRange)
    if(result1['matching_results'] < 8):
        result1 = queryDinner('')
    if(result2['matching_results'] < 8):
        result2 = queryDinner('')

    return makePlan(result1,result2)

def prefQueryBreakfastEgg(prefDict,alleg,calRange):
    proteinLikes = []
    if prefDict == {}:
        return queryBreakfast('')
    if prefDict['proteinDict']['eggs'] != 'dislike':
        proteinLikes.append('eggs')
    vegetableLikes = addLikes(prefDict['vegetableDict'])
    herbLikes = addLikes(prefDict['herbDict'])
    dairyLikes = addLikes(prefDict['dairyDict'])
    carbLikes = addLikes(prefDict['carbDict'])
    queryString = selectRandom(proteinLikes, vegetableLikes, herbLikes, dairyLikes, carbLikes)
    if queryString is not '':
        queryString += addCals(calRange)
        queryString += addAllergies(alleg)
    return queryBreakfast(queryString)

def prefQueryBreakfastSmooth(prefDict,alleg,calRange):
    if prefDict == {}:
        return queryBreakfast('')
    fruitLikes = addLikes(prefDict['fruitDict'])
    queryString = selectRandom(fruitLikes)
    if queryString is not '':
        queryString += addCals(calRange)
        queryString += addAllergies(alleg)
    return queryBreakfast(queryString)

def prefQueryLunch(prefDict,alleg,calRange):
    if prefDict == {}:
        return queryLunch('')
    proteinLikes = addLikes(prefDict['proteinDict'])
    carbLikes = addLikes(prefDict['carbDict'])
    vegetableLikes = addLikes(prefDict['vegetableDict'])
    herbLikes = addLikes(prefDict['herbDict'])
    dairyLikes = addLikes(prefDict['dairyDict'])
    queryString = selectRandom(proteinLikes, carbLikes, vegetableLikes, herbLikes, dairyLikes)
    if queryString is not '':
        queryString += addCals(calRange)
        queryString += addExcludes(prefDict['proteinDict'], prefDict['carbDict'], prefDict['vegetableDict'])
        queryString += addAllergies(alleg)
    return queryLunch(queryString)

def prefQueryDinner(prefDict,alleg,calRange):
    if prefDict == {}:
        return queryDinner('')
    proteinLikes = addLikes(prefDict['proteinDict'])
    carbLikes = addLikes(prefDict['carbDict'])
    herbLikes = addLikes(prefDict['herbDict'])
    vegetableLikes = addLikes(prefDict['vegetableDict'])
    spiceLikes = addLikes(prefDict['spiceDict'])
    queryString = selectRandom(proteinLikes, carbLikes, herbLikes, vegetableLikes, spiceLikes)
    if queryString is not '':
        queryString += addCals(calRange)
        queryString += addExcludes(prefDict['proteinDict'], prefDict['carbDict'], prefDict['vegetableDict'])
        queryString += addAllergies(alleg)
    return queryDinner(queryString)

def addAllergies(alleg):
    queryString = ''
    for i in range(len(alleg)):
        if alleg[i] != "":
            queryString += r',ingredients:!"%s"' % alleg[i]
    return queryString

def addExcludes(*args):
    queryString = ''
    for i in range(len(args)):
        if len(args[i]) != 0:
            for key in args[i]:
                if args[i][key] == 'dislike':
                    queryString += r',ingredients:!"%s"' % key
    return queryString

def addLikes(ingredientDict):
    likes = []
    for key in ingredientDict:
        if ingredientDict[key] == 'like':
            likes.append(key)
    return likes

def selectRandom(*args):
    queryString = ""
    for i in range(len(args)):
        if len(args[i]) != 0:
            queryString += random.choice(args[i]) + " "
    return queryString

def addServings(result,calRange):
    for i in range(len(result)):
        if result[i]['calories'] < calRange[0]:
            result[i]['calories'] = str(result[i]['calories']) + "," + str(int(calRange[0]/int(result[i]['calories'])))
        else:
            result[i]['calories'] = str(result[i]['calories']) + ",1"
    return result
