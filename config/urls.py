"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
=======
from django.conf.urls import url
from app import views
from main import views
from postapp import views
from member import views
>>>>>>> c53896f83341c69f90fa6d75f33101e801205c95

urlpatterns = [
    path('',include('member.urls')),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('borrow/', include('borrow.urls'))
=======
    #path('index/', views.index),
    #path('insert/', views.insert),
    path('app/', include('app.urls')),
    path('main/', include('main.urls')),
    path('postapp/', include('postapp.urls')),
    path('member/', include('member.urls'))


>>>>>>> c53896f83341c69f90fa6d75f33101e801205c95
]
