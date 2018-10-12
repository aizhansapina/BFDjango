from django.contrib import admin
from . import models


# Register your models here.

from .models import Post

admin.site.register(Post)

from .models import Comment

admin.site.register(Comment)
