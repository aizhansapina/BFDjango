from django.contrib import admin

# Register your models here.

from .models import Owner , Task

admin.site.register(Task)
admin.site.register(Owner)