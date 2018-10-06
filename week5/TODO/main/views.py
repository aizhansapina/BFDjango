from django.shortcuts import render , redirect
from datetime import date, timedelta
from .models import Owner, Task
from .forms import TaskForm
from django.http import Http404

# Create your views here.

def all_tasks(request):
    if request.method == "POST":
        Task.objects.all().delete()
        return redirect('all')
    else:
        todo_task = Task.objects.all()
        context = {
            'Tasks' : todo_task
        }
    return render(request, 'todo_list.html', context)

def completed_tasks(request):
    completed_task = Task.objects.filter(mark = True)
    completed = {
        'Tasks' : completed_task
    }
    return render(request, 'completed_todo_list.html', completed)

def todo_tasks(request):
    incompleted_task = Task.objects.filter(mark = False)
    incompleted = {
        'Tasks' : incompleted_task
    }
    return render(request, 'todo_list.html', incompleted)

def order_alphabet(request):
    ordered_tasks = Task.objects.order_by('task_name')
    ordered = {
        'Tasks' : ordered_tasks
    }
    return render(request, 'todo_list.html', ordered)

def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
        else:
            raise Http404
    else:
        form = TaskForm()
        context = {
            'form': form
        }
        return render(request , 'add.html' , context)

def task_detail(request , task_id):
    if request.method == 'POST':
        Task.objects.filter(id = task_id).delete()
        return redirect('../')
    try:
        task = Task.objects.get(id = task_id)
    except Task.DoesNotExist:
        raise Http404("Task not found")
    context = {
        'task': task
    }
    return render(request, 'task_detail.html', context)


def delete_all(request):
    Task.objects.all().delete()
    #context = {}
    #return render(request, 'todo_list.html', context)
    return redirect('all')