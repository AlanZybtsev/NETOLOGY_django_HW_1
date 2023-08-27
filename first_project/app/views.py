from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os



def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().time()
    msg = current_time.strftime("%H:%M:%S")
    template_name = 'app/time.html'
    return render(request, template_name, {'time': msg})


def workdir_view(request):
    try:
        path = '.'
        directory_files = os.listdir(path)
        template_name = 'app/workdir.html'
        return render(request, template_name, {'files': directory_files})
        # по аналогии с `time_view`, напишите код,
        # который возвращает список файлов в рабочей
        # директории
    except directory_filesDoesNotExist:
        raise NotImplemented
