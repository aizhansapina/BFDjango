from django.shortcuts import render , redirect
import datetime

# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from .models import Post , Comment

def hello(request):
    html = "<html><body>Hello</body></html>"
    return HttpResponse(html)

def all_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request , 'post/all.html' , context)

def post_page(request , post_id):
    try:
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post = post)
    except Post.DoesNotExist:
        raise Http404("There is no such task")
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'post/page.html', context)

def add_comment(request , post_id):
    if request.method == 'POST':
        post = Post.objects.get(id = post_id)
        author = request.user.username
        if author=='':
            author = 'Anonymus'
        text = request.POST['text']
        comment = Comment(author = author , text = text , post = post)
        comment.save()
        return redirect('all_posts')
    else:
        post = Post.objects.get(id = post_id)
        return render(request , 'comment/add.html' , {'post': post})

def add_post(request):
    if request.method == 'POST':
        author = request.user.username
        if author == '':
            return HttpResponse("You should be authorized")
        header = request.POST['header']
        content = request.POST['content']
        post = Post(author = author , header = header , content = content)
        post.save()
        return redirect('home')
    else:
        return render(request , 'post/add.html')

