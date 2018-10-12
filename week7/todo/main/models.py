from django.db import models
import datetime


class Owner(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)

    def __str__(self):
        return self.first_name+' '+self.last_name


class Task(models.Model):
    create_date = models.DateTimeField()
    due_date = models.DateTimeField()
    owner = models.ForeignKey(Owner , on_delete = models.CASCADE)
    done_status = models.BooleanField(default = True)





