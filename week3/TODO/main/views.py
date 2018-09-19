from django.shortcuts import render
from datetime import date, timedelta

# Create your views here.

def todo_tasks(request):
    tasks = [{
        'is_completed' : False,
        'Task' : 'Task {}'.format(i),
        'Created' : date.today().strftime("%d/%m/%y"),
        'Due' : (date.today() + timedelta(days = 2)).strftime("%d/%m/%y"),
        'Owner' : 'admin',
        'Mark' : 'Done'
    }
        for i in range(1,5)
    ]
    context = {
        'tasks' : tasks
    }
    return render(request, 'todo_list.html', context)

def completed_tasks(request):
    completed = {
        'is_completed' : True,
        'Task' : 'Task 0',
        'Created' : date.today().strftime("%d/%m/%y"),
        'Due' :(date.today() + timedelta(days = 2)).strftime("%d/%m/%y"),
        'Owner' : 'admin',
        'Mark' : 'Not Done'
    }
    context = {
        'completed' : completed
    }
    return render(request, 'completed_todo_list.html', completed)
