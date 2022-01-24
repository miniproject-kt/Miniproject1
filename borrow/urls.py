from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('posts/', views.index),
    path('postDetails/', views.index),
    path('postRegistry/', views.index)
]
