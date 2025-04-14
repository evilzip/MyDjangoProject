"""
Модуль для работы с суперпользователем
"""
from django.contrib import admin
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    """Класс для работы с суперпользователем

    Args:
        admin (_type_): _description_
    """
    list_display = ("id", "section")


admin.site.register(Task, TaskAdmin)

# Register your models here.
