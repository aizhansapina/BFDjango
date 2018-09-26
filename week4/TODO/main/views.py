from django.shortcuts import render
from datetime import date, timedelta
from .models import Owner, Tasks

# Create your views here.

def all_tasks(request):
    todo_task = Tasks.objects.all()
    context = {
        'Tasks' : todo_task
    }
    return render(request, 'todo_list.html', context)

def completed_tasks(request):
    completed_task = Tasks.objects.filter(mark = True)
    completed = {
        'Tasks' : completed_task
    }
    return render(request, 'completed_todo_list.html', completed)

def todo_tasks(request):
    incompleted_task = Tasks.objects.filter(mark = False)
    incompleted = {
        'Tasks' : incompleted_task
    }
    return render(request, 'todo_list.html', incompleted)

def order_alphabet(request):
    ordered_tasks = Tasks.objects.order_by('task_name')
    ordered = {
        'Tasks' : ordered_tasks
    }
    return render(request, 'todo_list.html', ordered)