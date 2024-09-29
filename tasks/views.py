import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from tasks.form import TaskSerializer
from tasks.services import create_new_task, delete_task, get_all_tasks, get_task_by_id, update_task


@csrf_exempt
@require_http_methods(["GET", "POST"])
def create_and_get_tasks(request) -> JsonResponse:
    try:
        if request.method == 'GET':
            tasks = get_all_tasks()  # Supongo que esta función retorna un QuerySet
            return JsonResponse({'tasks': list(tasks.values())}, status=200)

        elif request.method == 'POST':
            try:
                print('Enter in create_and_get_tasks POST')
                task = TaskSerializer(data=json.loads(request.body))
                new_task = create_new_task(task)
                return JsonResponse({'task': new_task.id})
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)

    except Exception as e:
        # Manejo general de errores
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def get_delete_and_update_tasks(request, task_id: int) -> JsonResponse:
    print('Enter in get_delete_and_update_tasks GET, PUT, DELETE')
    task = get_task_by_id(task_id)

    if task is None:
        return JsonResponse({'error': 'Task not found'}, status=404)

    try:
        if request.method == 'GET':
            task_serialized = TaskSerializer(task)
            return JsonResponse({'task': task_serialized.data}, status=200)
        elif request.method == 'PUT':
            new_task_data = json.loads(request.body)
            print('new_task_data:', new_task_data)
            task_updated = update_task(current_task=task, task_data=new_task_data)
            return JsonResponse({'task': task_updated.id}, status=200)
        elif request.method == 'DELETE':
            delete_task(task)
            return JsonResponse({'message': 'Task deleted successfully'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

    #Render the template
@require_http_methods(["GET"])
def task_manager_interface(request):
    return render(request, 'task_manager.html')