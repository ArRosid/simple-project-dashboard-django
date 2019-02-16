from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home),
    path('task_list/', views.TaskListView.as_view(), name='task_list'),
    path('task_list/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task_list/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('task_list/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task_list/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('task_list/<int:pk>/take/', views.take_task, name='task_take'),
    path('task_list/<int:pk>/done/', views.task_done, name='task_done'),
]
