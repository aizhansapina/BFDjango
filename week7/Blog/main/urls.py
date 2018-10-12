from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('all_posts' , views.all_posts , name = "all_posts"),
    path('post/<int:post_id>' , views.post_page , name = "post_page"),
    path('add_comment/<int:post_id>' , views.add_comment , name = "add_comment"),
    path('add_post' , views.add_post , name = "add_post"),
]