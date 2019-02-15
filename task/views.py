from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.utils import timezone
from .models import Task

def home(request):
    return HttpResponse("Welcome to Simple Project Dashboard")

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['task_name','task_desc']
    success_url = '/task_list'
    extra_context = {
        'title': 'Edit Task'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = '/task_list'

class TaskCreateView(CreateView):
    model = Task
    fields = ['task_name','task_desc']
    success_url = '/task_list'
    extra_context = {
        'title': 'Create Task'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

    def form_valid(self, form):
        form.instance.task_creator = self.request.user
        form.instance.task_created = timezone.now
        return super().form_valid(form)

def take_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.task_taker = request.user.username
    task.time_taken = timezone.now()
    task.save()
    return redirect('task_list')

def task_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.time_done = timezone.now()
    task.save()
    return redirect('task_list')
