from django.urls import path

from core.views import (contato, cursos, eventos, home, login, materiais,
                        sobre, time, users)

urlpatterns = [
    path('', home, name='home'),
    path('cursos/', cursos),
    path('sobre/', sobre),
    path('users/', users),
    path('eventos/', eventos),
    path('materiais/', materiais),
    path('time/', time),
    path('contato/', contato),
    path('login/', login),
]
