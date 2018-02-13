from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.template import loader

# Create your views here.
def index(request):
    context = {}
    return render(request, 'app/index.html', context)

def search(request):
    context = {}
    return render(request, 'app/MealPlanSearch.html', context)
