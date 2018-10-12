from django.db import models
import datetime

class Post(models.Model):
    author = models.CharField(max_length = 30)
    header = models.CharField(max_length = 30)
    content = models.CharField(max_length = 1000)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.header

class Comment(models.Model):
    author = models.CharField(max_length = 30)
    text = models.CharField(max_length = 200)
    create_date = models.DateTimeField(auto_now_add = True , blank = True)
    post = models.ForeignKey(Post , on_delete = models.CASCADE)