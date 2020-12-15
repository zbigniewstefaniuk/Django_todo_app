from django import forms
from django.forms import ModelForm

# DB import
from .models import Task


class TaskForm(forms.ModelForm):
    # making in html form with this class
    class Meta:
        model = Task
        fields = '__all__'
