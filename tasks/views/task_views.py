import json
from urllib.request import Request
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import redis

from tasks.form import TaskSerializer
from tasks.services.task_service import create_new_task, delete_task, get_all_tasks, get_task_by_id, update_task
from tasks.tasks import add, send_task_mail_notifiaction, test
from django.core.mail import send_mail


@method_decorator(csrf_exempt, name='dispatch')
class TaskListView(View):
    def get(self, request: Request) -> JsonResponse:
        try:
            tasks = get_all_tasks()
            return JsonResponse({'tasks': list(tasks.values())}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def post(self, request: Request) -> JsonResponse:
        try:
            task_data = json.loads(request.body)
            task = TaskSerializer(data=task_data)
            new_task = create_new_task(task)
            send_task_mail_notifiaction.delay('Nueva tarea asignada',
                f'''Se ha creado una nueva tarea: {new_task.title}\n
                descripcion: {new_task.description}''',['angel.de.oz.97@gmail.com'])
    
            return JsonResponse({'message': 'Task created successfully', 'taskId': new_task.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid input'}, status=400)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=500)
    
@method_decorator(csrf_exempt, name='dispatch')
class TaskDetailView(View):
    def get(self, request: Request, task_id: int) -> JsonResponse:
        task = get_task_by_id(task_id)
        if task:
            task_serialized = TaskSerializer(task)
            return JsonResponse({'task': task_serialized.data}, status=200)
        return JsonResponse({'error': 'Task not found'}, status=404)

    def put(self, request: Request, task_id: int) -> JsonResponse:
        task = get_task_by_id(task_id)
        if not task:
            return JsonResponse({'error': 'Task not found'}, status=404)
        try:
            new_task_data = json.loads(request.body)
            task_updated = update_task(current_task=task, task_data=new_task_data)
            return JsonResponse({'message': 'Task updated successfully', 'taskId': task_updated.id}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    def delete(self, request: Request, task_id: int) -> JsonResponse:
        task = get_task_by_id(task_id)
        if not task:
            return JsonResponse({'error': 'Task not found'}, status=404)
        delete_task(task)
        return JsonResponse({'message': 'Task deleted successfully'}, status=200)


class TaskManagerInterface(View):
    def get(self, request: Request):
        return render(request=request, template_name='task_manager.html')
