import json
import sys
import os
from watson_developer_cloud import DiscoveryV1

breakfast_discovery = DiscoveryV1(
    username = '',
    password = '',
    version = '2017-11-07'
)

lunch_discovery = DiscoveryV1(
    username = '',
    password = '',
    version = '2017-11-07'
)

dinner_discovery = DiscoveryV1(
    username = '7f31ee94-5960-4498-b9de-72fa3db9b234',
    password = 'ZH2Z1SNpWYD4',
    version = '2017-11-07'
)

breakfast_environment_id = ''
breakfast_collection_id = 'd2218b6c-b02d-4073-a3f4-de28fb145bcb'

lunch_environment_id = '6a487cbb-3a04-4f03-9f06-88084e3c2b6d'
lunch_collection_id = 'd2218b6c-b02d-4073-a3f4-de28fb145bcb'

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
