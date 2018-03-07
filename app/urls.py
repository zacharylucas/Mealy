from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
	path('conversation/', views.conversation, name='conversation'),
    path('preferenceSelection/', views.preferenceSelection, name='preferenceSelection')
]
