from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('completed_tasks' , views.completed_tasks , name = "completed_tasks"),
    path('all_tasks' , views.all_tasks),
    path('new_task' , views.new_task , name = "new_task"),
    path('task/<int:task_id>' , views.task_page , name = "task_page"),
]