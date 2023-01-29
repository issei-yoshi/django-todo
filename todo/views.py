from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy

from todo.models import Task

class TaskListView(ListView):
    model = Task

class TaskDetailView(DetailView):
    model = Task
    template_name = "todo/task_detail.html"

class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task-list")

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task-list")
    template_name = 'todo/task_delete.html'