"""
Модуль для обработки URL запросов с последущим вызовом
метода из модуля views
"""

from django.urls import path
from . import views
import django


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/result/', views.result, name='result'),
]

