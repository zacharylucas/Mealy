import requests
import re
import json
import time
import glob
import random
import time
from bs4 import BeautifulSoup
from watson_developer_cloud import NaturalLanguageClassifierV1

def get_minutes(element):
    try:
        tstring = element.get_text()
        if '-' in tstring:
            tstring = tstring.split('-')[1]  # some time formats are like this: '12-15 minutes'
        matched = TIME_REGEX.search(tstring)

        minutes = int(matched.groupdict().get('minutes') or 0)
        minutes += 60 * int(matched.groupdict().get('hours') or 0)

        return minutes
    except AttributeError:  # if dom_element not found or no matched
        return 0

def normalize_string(string):
    return re.sub(
        r'\s+', ' ',
        string.replace(
            '\xa0', ' ').replace(  # &nbsp;
            '\n', ' ').replace(
            '\t', ' ').strip()
    )

TIME_REGEX = re.compile(
    r'(\D*(?P<hours>\d+)\s*(hours|hrs|hr|h|Hours|H))?(\D*(?P<minutes>\d+)\s*(minutes|mins|min|m|Minutes|M))?'
)

natural_language_classifier = NaturalLanguageClassifierV1(
    username='22ee75e6-9b0d-4a73-b907-e565e55f1cab',
    password='bjOVSchN64CM'
)
# ID of the trained NLC (must be updated every time a new NLC is trained)
classifier_id = '8fc193x296-nlc-3501'

completed = 0 # number of completed recipes found
skipped = 0 # number of recipes skipped

start = 6500 # min ID
end = 300000 # max ID

# Get list of queryable IDs by removing previously queried IDs
ids = set(range(start,end))
queried_filename = 'recipes/queried_ids-DO-NOT-OPEN.txt'
with open(queried_filename, 'r') as infile:
    removable_ids = infile.readlines()
    for x in removable_ids:
        ids.remove(int(x))

# Loop over every ID until we run out
while len(ids)>0:
    # Sleep to not piss off allrecipes
    sleeptime = random.randint(2,3)
    print("........Sleeping for " + str(sleeptime) + " seconds........")
    time.sleep(sleeptime)     

    # Pull a random ID from our list 
    id = random.choice(list(ids))
    ids.remove(id)
    with open(queried_filename, 'a') as outfile:
        outfile.write(str(id) + '\n')
    print("  ID: " + str(id))

    # Collect and parse recipe page
    try:
        page = requests.get('http://allrecipes.com/recipe/' + str(id))
        soup = BeautifulSoup(page.text, "html.parser")

        # Get recipe title
        title = soup.find('h1').get_text()
        if title == 'Oh, snap!':
            skipped += 1
            print('  No title')
            continue # this id doesn't have an associated recipe

        # Get image url
        image_url = soup.find('img', {'class': 'rec-photo'})['src']
        if 'recipes/nophoto/nopicture' in image_url:
            skipped += 1
            print('  No image')
            continue

        # Get ratings
        rating = soup.find('div', {'class': 'rating-stars'})['data-ratingstars']
        if rating == '0':
            skipped += 1
            print('  No rating')
            continue

        # Get ready in time
        ready_in_minutes = get_minutes(soup.find('span', {'class': 'ready-in-time'}))
        if ready_in_minutes == 0:
            skipped += 1
            print('  No time')
            continue

        # Get calorie count
        calorie_count = soup.find('span', {'class': 'calorie-count'}).findAll('span')[0].text
        if calorie_count == 0:
            skipped += 1
            print('  No calories')
            continue

        # Get ingredients list
        ingredients_html = soup.findAll('li', {'class': "checkList__line"})
        ingredients_list = [
            normalize_string(ingredient.get_text().replace("ADVERTISEMENT", ""))
            for ingredient in ingredients_html
            if ingredient.get_text(strip=True) not in ('Add all ingredients to list', '', 'ADVERTISEMENT')
        ]
        if len(ingredients_list) == 0:
            skipped += 1
            print('  No ingredients')
            continue

        # Get instructions list
        instructions_html = soup.findAll('span', {'class': 'recipe-directions__list--item'})
        instructions_list = '\n'.join([
                    normalize_string(instruction.get_text())
                    for instruction in instructions_html
                ])
        if len(instructions_list) == 0:
            skipped += 1
            print('  No instructions')
            continue

        # Classify with NLC
        print('  Recipe: ' + title)
        classifications = natural_language_classifier.classify(classifier_id, title)
        classification = classifications['classes'][0]['class_name']
        print('  Class: ' + classification)

        # Create a file for this recipe in JSON
        recipe_object = ({"title": title, "rating": float(rating), "minutes": ready_in_minutes, "ingredients": ingredients_list, "instructions": instructions_list, "image": image_url})
        completed += 1
        filename = 'recipes/' + classification + '/recipe' + str(id) + '.json'
        print("  File: " + filename)
        with open(filename, 'w') as outfile:
            json.dump(recipe_object, outfile)
    except:
        print('  ~~~ERROR~~~')
        continue

# print results
print('................................')
print(str(completed) + " recipes stored")
print(str(skipped) + " recipes skipped")
