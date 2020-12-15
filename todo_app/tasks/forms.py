from django import forms
from django.forms import ModelForm

# DB import
from .models import Task


class TaskForm(forms.ModelForm):
    # adding custom css parameters to form field
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'todo-input',
            'placeholder': 'Add new task...'
        }))
    # making in html form with this class

    class Meta:
        model = Task
        fields = '__all__'
