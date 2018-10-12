from django.shortcuts import render , redirect
import datetime

# Create your views here.

from django.http import HttpResponse
from .models import Task,Owner
from .forms import TaskForm
from django.http import Http404

def hello(request):
    html = "<html><body>Hello</body></html>"
    return HttpResponse(html)

def all_tasks(request):
    tasks = Task.objects.all()
    todo_list = {
        'tasks': tasks
    }

    return render(request, 'todo_list.html', todo_list)

def completed_tasks(request):
    tasks = Task.objects.filter(done_status = True)

    todo_list = {
        'tasks': tasks
    }

    return render(request, 'completed_todo_list.html', todo_list)


def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        print(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('./all_tasks')
        else:
            html = "<html><body>Hello</body></html>"
            return HttpResponse(html)
    else:
        form = TaskForm()
        owners = Owner.objects.all()
        context = {
            'form': form,
            'owners': owners
        }
        return render(request, 'new_task.html', context)

def task_page(request , task_id):
    print(request)
    if request.method == 'POST':
        print(1)
        Task.objects.filter(id = task_id).delete()
        return redirect('../all_tasks')
    else:
        try:
            task = Task.objects.get(id = task_id)
        except Task.DoesNotExist:
            raise Http404("There is no such task")
        context = {
            'task': task
        }
        return render(request , 'task/page.html' , context)
