
import json
import sys
import os
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    username = '7f31ee94-5960-4498-b9de-72fa3db9b234',
    password = 'ZH2Z1SNpWYD4',
    version = '2017-11-07'
)

environment_id = '6a487cbb-3a04-4f03-9f06-88084e3c2b6d'
collection_id = 'd2218b6c-b02d-4073-a3f4-de28fb145bcb'
configuration_id = 'bf4f75b5-4849-465f-931a-35961d24a6fa'
collection_name = 'Recipe_Catalog'

def queryWatson(queryString, count = '', filters = ''):
    recipe_query = discovery.query(environment_id, collection_id, query=queryString)
    return recipe_query
