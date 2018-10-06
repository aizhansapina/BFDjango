from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts),
    path('add/', views.add, name="add"),
    path('post/<int:post_id>', views.post_detail, name="post_detail"),
    path('post/<int:post_id>/comments', views.post_comment, name='post_comment')
]
