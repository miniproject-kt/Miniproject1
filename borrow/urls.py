from django.urls import path, include
from . import views

urlpatterns = [
    path('category/', views.category, name = 'category'),
    path('map/', views.getMap)
]
