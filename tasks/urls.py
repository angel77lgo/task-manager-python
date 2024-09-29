
from django.urls import path

from tasks import views


urlpatterns = [
    path('tasks/', view=views.create_and_get_tasks, name='create_and_get_tasks'),
    path('tasks/<int:task_id>/', view=views.get_delete_and_update_tasks, name='get_delete_and_update_tasks'),
]