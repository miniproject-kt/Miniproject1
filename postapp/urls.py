from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('main/', views.main),
    path('category/', views.category, name = 'category'),
    path('form/post/', views.form_post, name = 'post'),
    path('post/<int:pk>/', views.detail, name = 'detail'),
    
]

urlpatterns +=static(settings.MEDIA_URL, document_root  = settings.MEDIA_ROOT)
