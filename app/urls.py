from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('search/', views.search, name='search'),
	path('conversation/', views.conversation, name='conversation'),
    path('preferenceSelection/', views.preferenceSelection, name='preferenceSelection'),
    path('chatbot/', views.chatbot, name = 'chatbot'),
    path('meals/', views.meals, name="meals"),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page': 'index'}, name='logout'),
    path('signup/', views.signup, name='signup')
]
