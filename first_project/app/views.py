from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os

def home(request):
    pages = [
        ('/current_time/','Показать текущее время'),
        ('/workdir/', 'Содержимое рабочей директории'),
    ]
    links = [f'<li><a href="{url}">{name}</a></li>' for url, name in pages]
    response = f"<h1>Доступные страницы:</h1><ul>{''.join(links)}</ul>"
    return HttpResponse(response)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = None
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    raise NotImplemented

def current_time(request):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(f"<h1>Текущие время:</h1><P>{now}</P>")

def workdir(requests):
    files = os.listdir('.')
    files_list = "<br>".join(files)
    return HttpResponse(f"<h1>Содержимое рабочей директории:</h1><p>{files_list}</p>")