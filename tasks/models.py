from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'tasks'