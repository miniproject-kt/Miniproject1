from django.urls import path
from . import views
app_name = "app"
urlpatterns = [
    path('mypage/', views.mypage),
    path('insert/', views.insert),
]