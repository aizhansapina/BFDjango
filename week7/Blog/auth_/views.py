from django.shortcuts import render , redirect
from django.http import HttpResponse , Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth

# Create your views here.

def home(request):
    return render(request , 'home.html')

def register(request):
    form = UserCreationForm(data = request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            raise Http404
    else:
        context = {
            'form': form
        }
        return render(request , 'registration.html' , context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username , password = password)
        if user is not None and user.is_active:
            auth.login(request , user)
            return redirect('home')
        else:
            error = "username or password incorrect"
            return render(request, 'login.html', {'error': error})
    else:
        return render(request , 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')




