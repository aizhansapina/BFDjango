from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_tasks),
    path('1/completed/', views.completed_tasks)
]
