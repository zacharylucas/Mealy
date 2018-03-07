from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
	path('conversation/', views.conversation, name='conversation'),
    path('chatbot/', views.chatbot, name = 'chatbot')
]
