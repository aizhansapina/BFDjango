from django.db import models
from datetime import datetime, timedelta


# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Task(models.Model):
    task_name = models.CharField(max_length = 100)
    created = models.DateField()
    due = models.DateField()
    owner = models.ForeignKey(Owner, on_delete = models.CASCADE)
    mark = models.BooleanField(default = False)

    def __str__(self):
        return self.task_name