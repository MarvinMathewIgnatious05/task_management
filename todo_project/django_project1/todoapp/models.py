from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    # task_id =models.IntegerField(null=True)
    task_title = models.CharField(max_length=225,null=True)
    task_complete = models.BooleanField(default=False,null=True)
    task_description = models.CharField(max_length=225,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.task_title)





