from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('register' , views.register , name = "register"),
    path('home' , views.home , name = "home"),
    path('login' , views.login , name = "login"),
    path('logout' , views.logout , name = "logout"),
]