
def createPreferences(request):
    proteinDict = {
        'chicken' : request.POST.get('radio-group-chicken'),
        'steak' : request.POST.get('radio-group-steak'),
        'beef' : request.POST.get('radio-group-beef'),
        'pork' : request.POST.get('radio-group-pork'),
        'eggs' : request.POST.get('radio-group-eggs'),
        'beans' : request.POST.get('radio-group-beans'),
        'tofu' : request.POST.get('radio-group-tofu')
    }
    carbDict = {
        'pasta' : request.POST.get('radio-group-pasta'),
        'white-bread' : request.POST.get('radio-group-white-bread'),
        'wheat-bread' : request.POST.get('radio-group-wheat-bread'),
        'rice' : request.POST.get('radio-group-rice'),
        'quinoa' : request.POST.get('radio-group-quinoa'),
        'whole-grains' : request.POST.get('radio-group-whole-grains')
    }
    fruitDict = {
        'bananas' : request.POST.get('radio-group-bananas'),
        'berries' : request.POST.get('radio-group-berries'),
        'melons' : request.POST.get('radio-group-melons'),
        'apples' : request.POST.get('radio-group-apples'),
        'citruses' : request.POST.get('radio-group-citruses'),
        'lemons' : request.POST.get('radio-group-lemons'),
        'lime' : request.POST.get('radio-group-lime')
    }
    vegetableDict = {
        'carrots' : request.POST.get('radio-group-carrots'),
        'squash' : request.POST.get('radio-group-squash'),
        'cucumbers' : request.POST.get('radio-group-cucumbers'),
        'peppers' : request.POST.get('radio-group-peppers'),
        'onions' : request.POST.get('radio-group-onions'),
        'celery' : request.POST.get('radio-group-celery'),
        'leafy-greens' : request.POST.get('radio-group-leafy-greens')
    }
    dairyDict = {
        'milk' : request.POST.get('radio-group-milk'),
        'yogurt' : request.POST.get('radio-group-yogurt'),
        'cheese' : request.POST.get('radio-group-cheese'),
        'skim-milk' : request.POST.get('radio-group-skim-milk')
    }
    spiceDict = {
        'garlic' : request.POST.get('radio-group-garlic'),
        'chili-powder' : request.POST.get('radio-group-chili-powder'),
        'cayenne' : request.POST.get('radio-group-cayenne'),
        'cumin' : request.POST.get('radio-group-cumin'),
        'ginger' : request.POST.get('radio-group-ginger'),
        'paprika' : request.POST.get('radio-group-paprika'),
        'saffron' : request.POST.get('radio-group-saffron'),
    }
    herbDict = {
        'oregano' : request.POST.get('radio-group-oregano'),
        'cilantro' : request.POST.get('radio-group-cilantro'),
        'thyme' : request.POST.get('radio-group-thyme'),
        'basil' : request.POST.get('radio-group-basil'),
        'parsley' : request.POST.get('radio-group-parsley'),
        'rosemary' : request.POST.get('radio-group-rosemary'),
        'mint' : request.POST.get('radio-group-mint'),
    }
    sweetDict = {
        'cake' : request.POST.get('radio-group-cake'),
        'pudding' : request.POST.get('radio-group-pudding'),
        'pie' : request.POST.get('radio-group-pie'),
        'ice-cream' : request.POST.get('radio-group-ice-cream'),
    }
    prefDict = {
        'proteinDict' : proteinDict,
        'carbDict' : carbDict,
        'fruitDict' : fruitDict,
        'vegetableDict' : vegetableDict,
        'dairyDict' : dairyDict,
        'spiceDict' : spiceDict,
        'herbDict' : herbDict,
        'sweetDict' : sweetDict,
    }
    return prefDict
