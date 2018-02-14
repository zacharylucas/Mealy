from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.template import loader

# Create your views here.
def search(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        #req = requests.get('https://api.github.com/users/' + username)
        #jsonList = []
        #jsonList.append(req.json())
        userData = {}
        userData['name'] = username
        '''
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        '''
        parsedData.append(userData)
    return render(request, 'app/search.html', {'data' : parsedData})
