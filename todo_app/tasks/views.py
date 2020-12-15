from django.shortcuts import render, redirect

# DB import
from .models import Task
from .forms import TaskForm

# Create your views here.


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'tasks/list.html', context)


def update_todo(request, pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'tasks/update_task.html', context)


def delete_todo(request, pk):
    todo = Task.objects.get(id=pk)

    if request.method == 'POST':
        todo.delete()
        return redirect('/')

    context = {
        'todo': todo
    }

    return render(request, 'tasks/delete.html', context)
