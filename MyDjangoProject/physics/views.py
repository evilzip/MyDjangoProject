"""Модуль вазывающийся при URL запросе через модуль urls"""
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from .models import Task


def homepage(request):
    """Функция вызыается при переходе по пути /home/

    Args:
        request: запрос от сайта

    Returns:
        HttpResponse: рендер страницы
    """
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())


@csrf_exempt
def quiz(request):
    """Функция вызыается при переходе по пути /quiz/
    Так же осуществляется валидация данных на сайте
    через метод POST

    Args:
        request: запрос от сайта

    Returns:
        HttpResponse: рендер страницы
    """
    tasks = Task.objects.all().values()
    template = loader.get_template('quiz.html')
    context = {
        'tasks': tasks,
    }

    if request.method == 'POST':
        uname = request.POST.get('uname')
        context['uname'] = uname

    return HttpResponse(template.render(context, request))


@csrf_exempt
def result(request):
    """Функция вызыается при переходе по пути /quiz/result/
    Так же осуществляется валидация данных на сайте
    через метод POST

    Args:
        request: запрос от сайта

    Returns:
        HttpResponse: рендер страницы
    """
    tasks = Task.objects.all().values()
    score = 0
    template = loader.get_template('result.html')

    if request.method == 'POST':
        tasks = Task.objects.all().values()
        score = 0
        #        uname = str(request.POST.get('uname'))
        for task in tasks:
            rs = task['id']
            ans = request.POST.get(f'{rs}')
            print(ans, task['answer'])

            if str(ans) == str(task['answer']):
                score += 1
        template = loader.get_template('result.html')

    context = {
        'score': score,
        # 'uname': uname,
    }
    return HttpResponse(template.render(context, request))


def custom_404(request, exception):
    return render(request, '404.html', status=404)

# Create your views here.
