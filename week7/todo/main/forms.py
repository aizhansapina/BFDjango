from django.forms import ModelForm
from main.models import Task
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('create_date', 'due_date', 'owner', 'done_status' )
