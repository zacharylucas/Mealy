from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.template import loader
from .Controllers import watsonQueries as wQ
from .Controllers import Conversation as con

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
            recipes.append(recipe)
        data = {'recipes' : recipes}
    return render(request, 'app/search.html', data)

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
    return render(request, 'app/index.html', context)

def conversation(request):
	context = {}
	return render(request, 'app/conversation.html', context)
