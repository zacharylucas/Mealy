from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.template import loader
from .Controllers import watsonQueries as wQ

# Create your views here.
def index(request):
    context = {}
    return render(request, 'app/index.html', context)

def detail(request, page_id):
    return HttpResponse("You're looking at app page %s." % page_id)
