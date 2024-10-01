#!/bin/bash
set -e  # Para que el script falle si algún comando falla

# Ejecutar migraciones
echo "Ejecutando migraciones..."
python manage.py migrate

# Iniciar Gunicorn
echo "Iniciando Gunicorn..."
exec gunicorn task_manager.wsgi:application --bind 0.0.0.0:8000