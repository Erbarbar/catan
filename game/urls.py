# game/urls.py
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('room/<str:room_name>/', views.room, name='room'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='game/login.html')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
]