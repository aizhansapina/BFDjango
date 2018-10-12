from django.contrib import admin
from . import models


# Register your models here.

from .models import Owner

admin.site.register(Owner)

from .models import Task

admin.site.register(Task)
