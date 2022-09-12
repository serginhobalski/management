from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'core/index.html')


def sobre(request):
    return render(request, 'core/sobre.html')


def cursos(request):
    return render(request, 'core/cursos.html')


def eventos(request):
    return render(request, 'core/eventos.html')


def materiais(request):
    return render(request, 'core/materiais.html')


def time(request):
    return render(request, 'core/time.html')


def contato(request):
    return render(request, 'core/contato.html')


def login(request):
    return render(request, 'core/login.html')


def users(request):
    return HttpResponse('<h1>USERS</h1')
