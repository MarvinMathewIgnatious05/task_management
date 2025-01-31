from django.contrib import admin
from .models import Task

# admin.site.register(Task)


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_title')
    fields = ("task_title", "task_complete", "task_description", "user")

    # readonly_fields = ("created_on",)
admin.site.register(Task, TaskAdmin)