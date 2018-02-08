import requests
import re
from bs4 import BeautifulSoup
import json
import time
import glob
import random

TIME_REGEX = re.compile(
    r'(\D*(?P<hours>\d+)\s*(hours|hrs|hr|h|Hours|H))?(\D*(?P<minutes>\d+)\s*(minutes|mins|min|m|Minutes|M))?'
)

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

recipes = { 'recipes' : {} }
completed = 0
skipped = 0
starting_file_number = 24

# Get recipe IDs from text files
recipe_ids = []
for filename in glob.iglob('recipe_ids/*.txt'):
    with open(filename, 'r') as id_file:
        ids = id_file.readlines()
        for id in ids:
            recipe_ids.append(int(id.replace('\n', '')))

# Append IDs of recipes that were not saved in previous run
recipe_ids.append(87605)
recipe_ids.append(15956)

for id in recipe_ids: #range(start, end):
    sleeptime = random.randint(2,5)
    print("Sleeping for " + str(sleeptime) + " seconds")
    time.sleep(sleeptime)
    print("Querying for ID: " + str(id))

    # Collect and parse recipe page
    try:
        page = requests.get('http://allrecipes.com/recipe/' + str(id))
        soup = BeautifulSoup(page.text, "html.parser")

        # Get recipe title
        title = soup.find('h1').get_text()
        if title == 'Oh, snap!':
            skipped += 1
            print('No title')
            continue # this id doesn't have an associated recipe

        # Get image url
        image_url = soup.find('img', {'class': 'rec-photo'})['src']
        if image_url == 'http://images.media-allrecipes.com/global/recipes/nophoto/nopicture-910x511.png':
            skipped += 1
            print('No image')
            continue

        # Get ratings
        rating = soup.find('div', {'class': 'rating-stars'})['data-ratingstars']
        if rating == '0':
            skipped += 1
            print('No rating')
            continue

        # Get ready in time
        ready_in_minutes = get_minutes(soup.find('span', {'class': 'ready-in-time'}))
        if ready_in_minutes == 0:
            skipped += 1
            print('No time')
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
            print('No ingredients')
            continue

        # Get instructions list
        instructions_html = soup.findAll('span', {'class': 'recipe-directions__list--item'})
        instructions_list = '\n'.join([
                    normalize_string(instruction.get_text())
                    for instruction in instructions_html
                ])
        if len(instructions_list) == 0:
            skipped += 1
            print('No instructions')
            continue

        # Add this recipe to our dictionary
        recipes['recipes'][(completed % 5)+1] = ({"id": id, "title": title, "rating": float(rating), "minutes": ready_in_minutes, "ingredients": ingredients_list, "instructions": instructions_list, "image": image_url})
        print('Recipe stored!')
        completed += 1

        # Print 5 recipes to a file
        if completed % 5 == 0:
            filename = 'recipes/recipes' + str(int(completed/5)-1+starting_file_number) + '.json'
            print("Printing " + filename)
            with open(filename, 'w') as outfile:
                json.dump(recipes, outfile)
            recipes = { 'recipes' : {} }
    except:
        print('ERROR')
        continue

print(str(completed) + " recipes stored")
print(str(skipped) + " recipes skipped")
print("Remaining recipes not saved to files: ")
print(recipes)
