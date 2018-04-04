
def createPreferences(form):
    proteinDict = {
        'chicken' : form.__dict__['data']['chicken'],
        'steak' : form.__dict__['data']['steak'],
        'beef' : form.__dict__['data']['beef'],
        'pork' : form.__dict__['data']['pork'],
        'bacon' : form.__dict__['data']['bacon'],
        'sausage' : form.__dict__['data']['sausage'],
        'ham' : form.__dict__['data']['ham'],
        'turkey' : form.__dict__['data']['turkey'],
        'lamb' : form.__dict__['data']['lamb'],
        'eggs' : form.__dict__['data']['eggs'],
        'beans' : form.__dict__['data']['beans'],
        'tofu' : form.__dict__['data']['tofu'],
        'fish' : form.__dict__['data']['fish'],
        'salmon' : form.__dict__['data']['salmon'],
        'tilapia' : form.__dict__['data']['tilapia'],
        'tuna' : form.__dict__['data']['tuna']
    }
    carbDict = {
        'pasta' : form.__dict__['data']['pasta'],
        'bread' : form.__dict__['data']['bread'],
        'rice' : form.__dict__['data']['rice'],
        'quinoa' : form.__dict__['data']['quinoa'],
        'whole_grain' : form.__dict__['data']['whole_grain'],
        'whole_wheat' : form.__dict__['data']['whole_wheat'],
        'tortilla' : form.__dict__['data']['tortilla'],
        'oat' : form.__dict__['data']['oat'],
        'cereal' : form.__dict__['data']['cereal'],
        'pita' : form.__dict__['data']['pita']
    }
    fruitDict = {
        'banana' : form.__dict__['data']['banana'],
        'strawberry' : form.__dict__['data']['strawberry'],
        'raspberry' : form.__dict__['data']['raspberry'],
        'blueberry' : form.__dict__['data']['blueberry'],
        'cantelope' : form.__dict__['data']['cantelope'],
        'pineapple' : form.__dict__['data']['pineapple'],
        'coconut' : form.__dict__['data']['coconut'],
        'grape' : form.__dict__['data']['grape'],
        'mango' : form.__dict__['data']['mango'],
        'pear' : form.__dict__['data']['pear'],
        'plum' : form.__dict__['data']['plum'],
        'peach' : form.__dict__['data']['peach'],
        'watermelon' : form.__dict__['data']['watermelon'],
        'apple' : form.__dict__['data']['apple'],
        'orange' : form.__dict__['data']['orange'],
        'lemon' : form.__dict__['data']['lemon'],
        'lime' : form.__dict__['data']['lime']
    }
    vegetableDict = {
        'carrot' : form.__dict__['data']['carrot'],
        'squash' : form.__dict__['data']['squash'],
        'cucumber' : form.__dict__['data']['cucumber'],
        'bell_pepper' : form.__dict__['data']['bell_pepper'],
        'onion' : form.__dict__['data']['onion'],
        'celery' : form.__dict__['data']['celery'],
        'tomato' : form.__dict__['data']['tomato'],
        'potato' : form.__dict__['data']['potato'],
        'broccoli' : form.__dict__['data']['broccoli'],
        'corn' : form.__dict__['data']['corn'],
        'mushroom' : form.__dict__['data']['mushroom'],
        'lettuce' : form.__dict__['data']['lettuce'],
        'spinach' : form.__dict__['data']['spinach'],
        'kale' : form.__dict__['data']['kale'],
        'sweet_potato' : form.__dict__['data']['sweet_potato'],
        'zucchini' : form.__dict__['data']['zucchini'],
        'cucumber' : form.__dict__['data']['cucumber'],
        'asparagus' : form.__dict__['data']['asparagus']
    }
    dairyDict = {
        'milk' : form.__dict__['data']['milk'],
        'yogurt' : form.__dict__['data']['yogurt'],
        'cheese' : form.__dict__['data']['cheese'],
        'american_cheese' : form.__dict__['data']['american_cheese'],
        'mozzerella' : form.__dict__['data']['mozzerella'],
        'provolone' : form.__dict__['data']['provolone'],
        'swiss' : form.__dict__['data']['swiss'],
        'goat_cheese' : form.__dict__['data']['goat_cheese'],
        'blue_cheese' : form.__dict__['data']['blue_cheese'],
        'skim_milk' : form.__dict__['data']['skim_milk'],
        'butter' : form.__dict__['data']['butter']
    }
    spiceDict = {
        'garlic' : form.__dict__['data']['garlic'],
        'chili_powder' : form.__dict__['data']['chili_powder'],
        'cayenne' : form.__dict__['data']['cayenne'],
        'cumin' : form.__dict__['data']['cumin'],
        'ginger' : form.__dict__['data']['ginger'],
        'paprika' : form.__dict__['data']['paprika'],
        'saffron' : form.__dict__['data']['saffron'],
        'cinnamon' : form.__dict__['data']['cinnamon'],
        'curry_powder' : form.__dict__['data']['curry_powder'],
        'tumeric' : form.__dict__['data']['tumeric'],
        'ginger' : form.__dict__['data']['ginger']
    }
    herbDict = {
        'oregano' : form.__dict__['data']['oregano'],
        'cilantro' : form.__dict__['data']['cilantro'],
        'thyme' : form.__dict__['data']['thyme'],
        'basil' : form.__dict__['data']['basil'],
        'parsley' : form.__dict__['data']['parsley'],
        'rosemary' : form.__dict__['data']['rosemary'],
        'mint' : form.__dict__['data']['mint'],
        'sage' : form.__dict__['data']['sage'],
        'bay_leaf' : form.__dict__['data']['bay_leaf']
    }
    prefDict = {
        'proteinDict' : proteinDict,
        'carbDict' : carbDict,
        'fruitDict' : fruitDict,
        'vegetableDict' : vegetableDict,
        'dairyDict' : dairyDict,
        'spiceDict' : spiceDict,
        'herbDict' : herbDict,
    }
    return prefDict
