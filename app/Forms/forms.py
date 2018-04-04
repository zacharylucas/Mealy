from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


DIET_PLAN_CHOICES = [
    ('loseWeight', 'Lose Weight'),
    ('maintainWeight', 'Maintain Weight'),
    ('gainWeight', "Gain Weight")
]

class UserInfoForm(forms.Form):
    dietary_restrictions = forms.CharField(max_length=100, required=False)
    food_allergies = forms.CharField(max_length=100, required=False)
    height = forms.IntegerField(label="Height (Inches)", required=True)
    weight = forms.IntegerField(label="Weight (Pounds)", required=True)
    diet_plan = forms.CharField(widget=forms.Select(choices=DIET_PLAN_CHOICES))
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    preferred_breakfast_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    preferred_lunch_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    preferred_dinner_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))


CHOICES = [
    ('like','Like'),
    ('','Neutral'),
    ('dislike','Dislike')
]

class PreferencesForm(forms.Form):
    chicken = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    steak = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    beef = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    pork = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    bacon = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    sausage = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    ham = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    turkey = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    lamb = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    eggs = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    beans = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    fish = forms.ChoiceField(label="Fish (General)", choices=CHOICES, widget=forms.RadioSelect(), required=False)
    tofu = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    salmon = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    tilapia = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    tuna = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)

    pasta = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    bread = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    rice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    quinoa = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    whole_grain = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    whole_wheat = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    tortilla = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    oat = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    cereal = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    pita = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)

    banana = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    strawberry = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    raspberry = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    blueberry = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    cantelope = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    pineapple = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    coconut = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    grape = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    mango = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    pear = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    plum = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    peach = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    watermelon = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    apple = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    orange = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    lemon = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    lime = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)

    carrot = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    squash = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    cucumber = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    bell_pepper = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    onion = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    celery = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    tomato = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    potato = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    broccoli = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    corn = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    mushroom = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    lettuce = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    spinach = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    kale = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    sweet_potato = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    zucchini = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    cucumber = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    asparagus = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)

    milk = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    yogurt = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    cheese = forms.ChoiceField(label="Cheese (General)", choices=CHOICES, widget=forms.RadioSelect(), required=False)
    american_cheese = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    mozzerella = forms.ChoiceField(label="Mozzerella Cheese", choices=CHOICES, widget=forms.RadioSelect(), required=False)
    provolone = forms.ChoiceField(label="Provolone Cheese", choices=CHOICES, widget=forms.RadioSelect(), required=False)
    swiss = forms.ChoiceField(label="Swiss Cheese", choices=CHOICES, widget=forms.RadioSelect(), required=False)
    goat_cheese = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    blue_cheese = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    skim_milk = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    butter = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)

    garlic = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    chili_powder = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    cayenne = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    cumin = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    ginger = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    paprika = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    saffron = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    cinnamon = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    cinnamon = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    curry_powder = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    tumeric = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    ginger = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)

    oregano = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    cilantro = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    thyme = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    basil = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    parsley = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    rosemary = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    mint = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    sage = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    bay_leaf = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
