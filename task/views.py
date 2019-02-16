from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Task

# @login_required
def home(request):
    return render(request, 'task/home.html')

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['task_name','task_desc']
    success_url = '/task_list'
    extra_context = {
        'title': 'Edit Task'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = '/task_list'

class TaskCreateView(LoginRequiredMixin, CreateView):
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
