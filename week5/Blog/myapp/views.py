from django.shortcuts import render , redirect
from datetime import date, timedelta
from .models import Post, Comment
from .forms import PostForm
from django.http import Http404

# Create your views here.
def all_posts(request):
    all = Post.objects.all()
    context = {
        'Posts': all
    }
    return render(request, 'post.html', context)
def add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
        else:
            raise Http404
    else:
        form = PostForm()
        context = {
            'form': form
        }
        return render(request , 'add.html' , context)