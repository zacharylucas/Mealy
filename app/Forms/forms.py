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
    ('dislike','Dislike')
]

class PreferencesForm(forms.Form):
    chicken = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    steak = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    beef = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    pork = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    bacon = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    sauage = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    ham = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    turkey = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    lamb = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    eggs = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    beans = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    fish = forms.ChoiceField(label="Fish (General)", choices=CHOICES, widget=forms.RadioSelect())
    tofu = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    salmon = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    tilapia = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    tuna = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    pasta = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    bread = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    rice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    quinoa = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    whole_grain = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    whole_wheat = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    tortilla = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    oat = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    cereal = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    pita = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    banana = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    strawberry = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    raspberry = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    blueberry = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    cantelope = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    pinapple = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    coconut = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    grape = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    mango = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    pear = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    plum = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    peach = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    watermelon = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    apple = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    oragne = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    lemon = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    lime = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    carrot = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    squash = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    cucumber = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    bell_pepper = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    onion = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    celery = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    tomato = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    potato = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    broccoli = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    corn = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    mushroom = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    lettuce = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    spinach = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    kale = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    sweet_potato = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    zucchini = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    cucumber = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    asparagus = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    milk = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    yogurt = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    cheese = forms.ChoiceField(label="Cheese (General)", choices=CHOICES, widget=forms.RadioSelect())
    american_cheese = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    mozzerella = forms.ChoiceField(label="Mozzerella Cheese", choices=CHOICES, widget=forms.RadioSelect())
    provolone = forms.ChoiceField(label="Provolone Cheese", choices=CHOICES, widget=forms.RadioSelect())
    swiss = forms.ChoiceField(label="Swiss Cheese", choices=CHOICES, widget=forms.RadioSelect())
    goat_cheese = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    blue_cheese = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    skim_milk = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    butter = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    garlic = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    chili_powder = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    cayenne = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    cumin = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    ginger = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    paprika = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    saffron = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    cinnamon = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    cinnamon = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    curry_powder = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    tumeric = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    ginger = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    oregano = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    cilantro = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    thyme = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    basil = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    parsley = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    rosemary = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    mint = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    sage = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    bay_leaf = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
