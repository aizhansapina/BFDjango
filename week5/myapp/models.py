from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'comment by '+ self.author