from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tasks),
    path('1/completed/', views.completed_tasks),
    path('1/todo/', views.todo_tasks),
    path('order/', views.order_alphabet)

]
