from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.template import loader
from .Controllers import watsonQueries as wQ

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

def index(request):
    context = {}
    return render(request, 'app/index.html', context)

def conversation(request):
	context = {}
	return render(request, 'app/conversation.html', context)

def preferenceSelection(request):
    context = {}
    return render(request, 'app/preferenceSelection.html', context)
