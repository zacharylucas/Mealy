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

# Create your views here.
def search(request):
    data = {}
    if request.method == 'POST':
        searchTerm = request.POST.get('user')
        query = wQ.queryWatson(searchTerm)
        #numResults = int(query['matching_results'])
        recipes = []
        for currentRecipe in query['results']:
            print(currentRecipe)
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

def meals(request):
    data = {}
    if request.method == 'GET':
        preferences = request.session['prefDict']
        breakfastQueryResults = wQ.breakfastPlan(preferences)
        lunchQueryResults = wQ.lunchPlan(preferences)
        dinnerQueryResults = wQ.dinnerPlan(preferences)
        data = {'breakfasts' : breakfastQueryResults, 'lunches' : lunchQueryResults, 'dinners' : dinnerQueryResults}

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
    context = {}
    if str(request.user) != 'AnonymousUser':
        prefDict = m.getPrefDict(request.user)
        request.session['prefDict'] = prefDict
        mealDict = m.getMealDict(request.user)
        request.session['mealDict'] = mealDict
        print(prefDict)
        
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
        return redirect('preferenceSelection')
        #if form.is_valid():
            #form.save()
    else:
        form = UserInfoForm()
    return render(request, 'app/userInfo.html', {'form' : form})

def preferenceSelection(request):
    if request.method == 'POST':
        form = PreferencesForm(request.POST)
        prefDict = pref.createPreferences(form)
        request.session['prefDict'] = prefDict
        if str(request.user) != 'AnonymousUser':
            m.updatePrefDict(request.user, prefDict)
        return redirect('meals')
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
