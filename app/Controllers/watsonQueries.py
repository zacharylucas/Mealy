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
breakfast_collection_id = 'dd40dded-24af-4444-a77d-36454cf954a5'

lunch_environment_id = 'e8a03832-1ad4-4c57-a8a9-4d4b3ae99d6e'
lunch_collection_id = '0d504254-4cb3-43e9-bb20-12b44faa3f76'

dinner_environment_id = '6a487cbb-3a04-4f03-9f06-88084e3c2b6d'
dinner_collection_id = 'f8d8da1b-414c-4ec6-b8d8-3082e25462f0'

def queryWatson(queryString, count = ''):
    recipe_query = dinner_discovery.query(dinner_environment_id, dinner_collection_id, query= queryString, count = count)
    return recipe_query

def queryBreakfast(queryString, count = ''):
    recipe_query = breakfast_discovery.query(breakfast_environment_id, breakfast_collection_id, query= queryString, count = count)
    return recipe_query

def queryLunch(queryString, count = ''):
    recipe_query = lunch_discovery.query(lunch_environment_id, lunch_collection_id, query= queryString, count = count)
    return recipe_query

def queryDinner(queryString, count = ''):
    recipe_query = dinner_discovery.query(dinner_environment_id, dinner_collection_id, query= queryString, count = count)
    return recipe_query

def prefQueryBreakfast(prefDict):
    proteinLikes = ['eggs']
    vegetableLikes = addLikes(prefDict['vegetableDict'])
    fruitLikes = addLikes(prefDict['fruitDict'])
    queryString = selectRandom(proteinLikes, vegetableLikes)
    queryString2 = selectRandom(fruitLikes)
    return queryBreakfast(random.choice([queryString, queryString2]))

def prefQueryLunch(prefDict):
    proteinLikes = addLikes(prefDict['proteinDict'])
    carbLikes = addLikes(prefDict['carbDict'])
    queryString = selectRandom(proteinLikes, carbLikes)
    return queryLunch(queryString)

def prefQueryDinner(prefDict):
    proteinLikes = addLikes(prefDict['proteinDict'])
    carbLikes = addLikes(prefDict['carbDict'])
    herbLikes = addLikes(prefDict['herbDict'])
    queryString = selectRandom(proteinLikes, carbLikes, herbLikes)
    return queryDinner(queryString)

def addLikes(ingredientDict):
    likes = []
    for key in ingredientDict:
        if ingredientDict[key] == 'like':
            likes.append(key)
    return likes

def selectRandom(*args):
    queryString = ""
    for i in range(len(args)):
        queryString += random.choice(args[i]) + " "
    return queryString
