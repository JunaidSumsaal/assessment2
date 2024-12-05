# TaskManager/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tasks.urls')),  # Use the task_list view for the root URL
    path('admin/', admin.site.urls),
]
