from django.shortcuts import render
from django.views.generic import ListView, DetailView

from todo.models import Task

class TaskListView(ListView):
    model = Task

class TaskDetailView(DetailView):
    model = Task
    template_name = "todo/task_detail.html"