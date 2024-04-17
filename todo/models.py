from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True, max_length=250)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    