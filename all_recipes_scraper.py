import requests
import re
from bs4 import BeautifulSoup
import json

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

for i in [14646,244558,261842]:
    # Collect and parse recipe page
    page = requests.get('http://allrecipes.com/recipe/' + str(i))
    soup = BeautifulSoup(page.text, "html.parser")

    # Get recipe title
    title = soup.find('h1').get_text()
    if title == 'Oh, snap!':
        continue # this id doesn't have an associated recipe

    # Get ready in time
    ready_in_minutes = get_minutes(soup.find('span', {'class': 'ready-in-time'}))

    # Get ingredients list
    ingredients_html = soup.findAll('li', {'class': "checkList__line"})
    ingredients_list = [
        normalize_string(ingredient.get_text().replace("ADVERTISEMENT", ""))
        for ingredient in ingredients_html
        if ingredient.get_text(strip=True) not in ('Add all ingredients to list', '', 'ADVERTISEMENT')
    ]

    # Get instructions list
    instructions_html = soup.findAll('span', {'class': 'recipe-directions__list--item'})
    instructions_list = '\n'.join([
                normalize_string(instruction.get_text())
                for instruction in instructions_html
            ])

    # Get image url
    image_url = soup.find('img', {'class': 'rec-photo'})['src']
    if image_url == 'http://images.media-allrecipes.com/global/recipes/nophoto/nopicture-910x511.png':
        continue # don't want meals without images? we can decide on this later

    # Add this recipe to our dictionary
    recipes['recipes'][str(i)] = ({"title": title, "minutes": ready_in_minutes, "ingredients": ingredients_list, "instructions": instructions_list, "image": image_url})

# Convert the recipe dictionary to a JSON object
output = json.dumps(recipes)
print(output)