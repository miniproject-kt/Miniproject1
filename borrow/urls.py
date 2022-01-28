from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('category/', views.category, name = 'category'),
    path('form/post/', views.form_post, name = 'post'),
    path('post/<int:pk>/', views.detail, name = 'detail'),
    path('map/', views.getMap)
]

# urlpatterns +=static(settings.MEDIA_URL, document_root  = settings.MEDIA_ROOT)