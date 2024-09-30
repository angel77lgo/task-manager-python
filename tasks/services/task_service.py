from tasks.form import TaskSerializer
from tasks.models.task_model import Task
from tasks.types import TaskCreate

def get_all_tasks() -> list[Task]:
    return Task.objects.all().order_by('-updated_at')


def get_task_by_id(task_id: int) -> Task | None:
    try:
        task = Task.objects.get(id=task_id)
        if task:
           return task
    except Task.DoesNotExist:
        return None


def create_new_task(new_task: TaskSerializer) -> Task:
    if new_task.is_valid(raise_exception=True):
        task = new_task.save()
        return task
    else:
        raise ValueError('Invalid input')
  


def update_task(current_task: Task, task_data: TaskCreate) -> Task:
    new_task = TaskSerializer(instance=current_task, data=task_data, partial=True)
    if new_task.is_valid():
        task = new_task.save()
        return task

def delete_task(task: Task) -> None:
    task.delete()