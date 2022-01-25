from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    # 직접 구현
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('login/valid/', views.valid_login, name = 'valid_login'),
    path('login/find/', views.find, name = 'find'),
]