"""
Модуль для создания объектов в базе данных и работе с ними
"""

from django.db import models

# Create your models here.


class Task(models.Model):
    """Класс для работы с заданием.
       Создается база данных Task где будут лежать
       условия задач
    """
    section = models.CharField('Раздел', max_length=50)
    task = models.TextField('Задача')
    answer = models.IntegerField('Ответ')

    def __str__(self):
        return (f"{self.id}{self.section}")


# Create your models here.
