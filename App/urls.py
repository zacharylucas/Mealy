from django.urls import path

from . import views

urlpatterns = [
    # ex: /search/
    path('search/', views.search, name='search'),
    path('MealPlanSearch/',views.MealPlanSearch, name='MealPlanSearch'),
]