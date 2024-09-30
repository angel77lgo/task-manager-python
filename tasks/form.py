import re

from rest_framework import serializers

from tasks.models.task_model import Task


def validate_email(value):
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
        raise serializers.ValidationError('Email address is invalid.')
    return value


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'email', 'description', 'due_date']
        read_only_fields = ['id']