from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.contrib.auth import login, authenticate

from .Controllers import watsonQueries as wQ
from .Controllers import Conversation as con
from .Controllers import Preference as pref
from .Controllers import DatabaseController as DB
from .models import User
from .Forms.forms import SignUpForm
from .Forms.forms import UserInfoForm
from .Forms.forms import PreferencesForm
from . import models as m
import re

# Create your views here.
def search(request):
    data = {}
    if request.method == 'POST':
        searchTerm = request.POST.get('user')
        query = wQ.queryWatson(searchTerm)
        #numResults = int(query['matching_results'])
        recipes = []
        for currentRecipe in query['results']:
            recipe = {}
            recipe['image'] = currentRecipe['image']
            recipe['title'] = currentRecipe['title']
            recipe['id'] = currentRecipe['id']
            recipe['minutes'] = currentRecipe['minutes']
            recipe['rating'] = currentRecipe['rating']
            recipe['ingredients'] = currentRecipe['ingredients']
            recipe['instructions'] = currentRecipe['instructions']
            recipes.append(recipe)
        data = {'recipes' : recipes}
        DB.showUser()
    return render(request, 'app/search.html', data)

def newMealPlan(request):
    preferences = {}
    if request.session.get('prefDict') != None:
        preferences = request.session['prefDict']

    alleg = []
    TDEE = 0
    if str(request.user) != 'AnonymousUser':
        if request.session.get('userDict') != None or request.session.get('userDict') != {}:
            if request.session.get('userDict') != None:
                if re.match('^[A-Za-z, ]*$', request.session['userDict']['allergy']):
                    alleg = re.split(', ',request.session['userDict']['allergy'])
                if request.session['userDict']['sex'] == "male":
                    TDEE = 655+ (9.6 * (2.2 * int(request.session['userDict']['weight']))) + (1.8 * (2.54 * int(requst.session['userDict']['height']))) - 4.7*int(request.session['userDict']['age'])
                else:
                    TDEE = 66+ (13.7 * (2.2 * int(request.session['userDict']['weight']))) + (5 * (2.54 * int(requst.session['userDict']['height']))) - 6.8*int(request.session['userDict']['age'])

    activity = [1.2, 1.375, 1.55, 1.725]
    TDEE = TDEE * activity[request.session['userDict']['activity_level']]
    calRange = []
    if request.session['userDict']['diet_plan'] == "lose_weight":
        calRange = [0, TDEE - 300]
    elif request.session['userDict']['diet_plan'] == "maintain_weight":
        calRange = [TDEE - 300, TDEE + 300]
    else:
        calRange = [TDEE + 300, TDEE +2000]

    breakfastCalRange = [x * .25 for x in calRange]
    lunchCalRange = [x * .35 for x in calRange]
    dinnerCalRange = [x * .40 for x in calRange]


    breakfastQueryResults = wQ.breakfastPlan(preferences,alleg)
    lunchQueryResults = wQ.lunchPlan(preferences,alleg)
    dinnerQueryResults = wQ.dinnerPlan(preferences,alleg)
    data = {'breakfasts' : breakfastQueryResults, 'lunches' : lunchQueryResults, 'dinners' : dinnerQueryResults}
    request.session['mealDict'] = data
    if str(request.user) != 'AnonymousUser':

        newUserDict = {}
        if request.session.get('userDict') != None or request.session.get('userDict') != {}:
                newUserDict =  request.session.get('userDict')

        m.updateAllDB(request.user, preferences, data, newUserDict)

    return data

def meals(request):
    data = {}
    if request.method == 'GET':
        if request.session.get('mealDict') == None or request.session.get('mealDict') == {}:
            data = newMealPlan(request)
        else:
            data = request.session['mealDict']
    elif request.method == 'POST':
        data = newMealPlan(request)

    return render(request, 'app/meals.html', data)

def chatbot(request):
    data = {}
    messages = []
    if request.method == 'GET':
        response = con.sendInitialMessage()

    if request.method == 'POST':
        userInput = request.POST.get('chat')
        response = con.sendMessage(userInput, request.session['context'])
        messages = request.session['messages']
        messages.insert(0,"User: " + userInput)

    messages.insert(0, "Chatbot: " + response['output']['text'][0])
    request.session['messages'] = messages
    request.session['context'] = response['context']
    data = {'messages' : messages}
    return render(request, 'app/chatbot.html', data)

def index(request):
    #print(str(request.user))
    context = {}
    if str(request.user) != 'AnonymousUser':
        prefDict = m.getPrefDict(request.user)
        request.session['prefDict'] = prefDict
        mealDict = m.getMealDict(request.user)
        request.session['mealDict'] = mealDict

    return render(request, 'app/index.html', context)

def conversation(request):
	context = {}
	return render(request, 'app/conversation.html', context)

def userInfo(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if  str(request.user) != 'AnonymousUser':
            r = form.__dict__['data']['dietary_restrictions']
            a = form.__dict__['data']['food_allergies']
            hi = form.__dict__['data']['height']
            wi = form.__dict__['data']['weight']
            g = form.__dict__['data']['diet_plan']
            p = form.__dict__['data']['phone_number']
            b = form.__dict__['data']['preferred_breakfast_time']
            l = form.__dict__['data']['preferred_lunch_time']
            d = form.__dict__['data']['preferred_dinner_time']
            glma = 3
            if g == 'loseWeight':
                glma = 2
            elif g == 'gainWeight':
                glma = 1
            m.updateUserInfo(request.user,  w=wi, h=hi, glm=glma, phone=p, btime=b,
                    ltime=l, dtime=d, restrict=r, allergy=a)
            newPrefDict = {}
            newMealDict = {}
            if request.session.get('mealDict') != None or request.session.get('mealDict') != {}:
                    newMealDict = request.session.get('mealDict')
            if request.session.get('prefDict') != None or request.session.get('prefDict') != {}:
                    newPrefDict =  request.session.get('prefDict')
            request.session['userDict'] = {
                'weight' : wi,
                'height' : hi,
                'glm' : glma,
                'restrict' : r,
                'allergy' : a,
                'phone' : p,
                'btime' : b,
                'ltime' : l,
                'dtime' : d
            }
            m.updateAllDB(request.user, newPrefDict, newMealDict, request.session['userDict'])
        else:
            r = form.__dict__['data']['dietary_restrictions']
            a = form.__dict__['data']['food_allergies']
            hi = form.__dict__['data']['height']
            wi = form.__dict__['data']['weight']
            g = form.__dict__['data']['diet_plan']
            p = form.__dict__['data']['phone_number']
            b = form.__dict__['data']['preferred_breakfast_time']
            l = form.__dict__['data']['preferred_lunch_time']
            d = form.__dict__['data']['preferred_dinner_time']
            glma = 3
            if g == 'loseWeight':
                glma = 2
            elif g == 'gainWeight':
                glma = 1
            m.updateUserInfo(request.user,  w=wi, h=hi, glm=glma, phone=p, btime=b,
                    ltime=l, dtime=d, restrict=r, allergy=a)
            request.session['userDict'] = {
                'weight' : wi,
                'height' : hi,
                'glm' : glma,
                'restrict' : r,
                'allergy' : a,
                'phone' : p,
                'btime' : b,
                'ltime' : l,
                'dtime' : d
            }

        return redirect('index')
        #if form.is_valid():
            #form.save()
    elif str(request.user) != 'AnonymousUser':
        dicti = m.getUserInfo(request.user)
        if dicti['gain_lose_maintain'] == 3:
            s = 'maintainWeight'
        elif dicti['gain_lose_maintain'] == 2:
            s = 'loseWeight'
        else:
            s = 'gainWeight'

        form = UserInfoForm(
                initial= {
                    'dietary_restrictions': dicti['dietRestrict'],
                    'food_allergies':dicti['allergies'],
                    'height':dicti['height'],
                    'weight':dicti['weight'],
                    'diet_plan':s,
                    'phone_number':dicti['cell'],
                    'preferred_breakfast_time':dicti['breakTime'],
                    'preferred_lunch_time':dicti['lunchTime'],
                    'preferred_dinner_time':dicti['dinnerTime']
                    })
    elif request.session.get('userDict') != None or request.session.get('userDict') != {}:
        if request.session.get('userDict') != None:
            glma = request.session['userDict']['glm']
            if glma == 3:
                s = 'maintainWeight'
            elif glma == 2:
                s = 'loseWeight'
            else:
                s = 'gainWeight'
            form = UserInfoForm(
                    initial= {
                        'dietary_restrictions': request.session['userDict'] ['restrict'],
                        'food_allergies':request.session['userDict'] ['allergy'],
                        'height':request.session['userDict'] ['height'],
                        'weight':request.session['userDict'] ['weight'],
                        'diet_plan':s,
                        'phone_number':request.session['userDict']['cell'],
                        'preferred_breakfast_time':request.session['userDict']['breakTime'],
                        'preferred_lunch_time':request.session['userDict']['lunchTime'],
                        'preferred_dinner_time':request.session['userDict']['dinnerTime']
                        })
        else:
            form = UserInfoForm(
                initial= {
                    'dietary_restrictions': '',
                    'food_allergies':'',
                    'height':0,
                    'weight':0,
                    'diet_plan':'maintainWeight',
                    })
    else:
        form = UserInfoForm(
                initial= {
                    'dietary_restrictions': '',
                    'food_allergies':'',
                    'height':0,
                    'weight':0,
                    'diet_plan':'maintainWeight',
                    })
    return render(request, 'app/userInfo.html', {'form' : form})

def preferenceSelection(request):
    if request.method == 'POST':
        form = PreferencesForm(request.POST)
        prefDict = pref.createPreferences(form)
        request.session['prefDict'] = prefDict
        if str(request.user) != 'AnonymousUser':

            newUserDict = {}
            newMealDict = {}
            if request.session.get('mealDict') != None or request.session.get('mealDict') != {}:
                    newMealDict = request.session.get('mealDict')
            if request.session.get('userDict') != None or request.session.get('userDict') != {}:
                    newUserDict =  request.session.get('userDict')

            m.updateAllDB(request.user, prefDict, newMealDict, newUserDict)

        return redirect('meals')
    else:
        if request.session.get('prefDict') != None and request.session.get('prefDict') != {}:
            form = pref.populatePreferences(request)
        else:
            form = PreferencesForm()
    return render(request, 'app/preferenceSelection.html', {'form' : form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            m.createUserInfo(user)
            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'app/signup.html', {'form': form})
