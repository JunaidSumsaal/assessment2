# tasks/views.py

from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()  # Get all tasks from the database
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
