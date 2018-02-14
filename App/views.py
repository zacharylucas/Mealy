from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.template import loader

# Create your views here.
def index(request):
    context = {queryWatson()}
    return render(request, 'app/index.html', context)

def detail(request, page_id):
    return HttpResponse("You're looking at app page %s." % page_id)
