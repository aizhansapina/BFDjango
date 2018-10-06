from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tasks, name = "all"),
    path('completed/', views.completed_tasks , name = "completed"),
    path('todo/', views.todo_tasks , name = "todo"),
    path('order/', views.order_alphabet),
    path('add/' ,views.add , name = "add" ),
    path('task/<int:task_id>' , views.task_detail , name = "task_detail"),
]