from django.shortcuts import render
from django.http import HttpResponse



# Create your views her
def index(request):
    return HttpResponse("Hello, World! You're at the polls index.")
