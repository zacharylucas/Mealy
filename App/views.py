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
        numResults = query['matching_results']
        recipes = []
        for i in range(numResults):
            recipe = {}
            recipe['image'] = query['result'][i]['image']
            recipe['title'] = query['result'][i]['title']
            recipes.append(recipe)
        data = {'recipes' : recipes}
    return render(request, 'app/search.html', data)