from django.contrib.auth.models import User

def createUser():
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

def showUser():
    print(User.objects.all())
