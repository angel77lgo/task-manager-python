
from django.urls import path

from tasks.views.task_views import TaskDetailView, TaskListView, TaskManagerInterface


urlpatterns = [
    path('', TaskManagerInterface.as_view(), name='task_manager_interface'),  # Para /task-manager/
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('tasks/<int:task_id>/', TaskDetailView.as_view(), name='get_delete_and_update_tasks'),
]