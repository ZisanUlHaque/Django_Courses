from django.db import models

class Task(models.Model):
    taskTitle = models.CharField(max_length=255)  
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField()

    def __str__(self):
        return self.taskTitle
