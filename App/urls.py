from django.urls import path

from . import views

urlpatterns = [
    # ex: /app/
    path('', views.index, name='index'),
    # ex: /app/5/
    path('<int:page_id>/', views.detail, name='detail'),
]