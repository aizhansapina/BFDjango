from django.urls import path
from . import views

urlpatterns = [
    path('hello' , views.hello , name = 'hello'),
    path('home' , views.home , name = 'home'),
    path('login' , views.login , name = 'login'),
    path('registration' , views.registration , name = 'registration'),
]