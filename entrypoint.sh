#!/bin/bash
set -e  # Para que el script falle si algún comando falla

# Ejecutar migraciones
python manage.py migrate

# Iniciar Gunicorn
exec gunicorn --bind 0.0.0.0:8000 task_manager.wsgi:application