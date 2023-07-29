from django.contrib import admin
from django.urls import path
from .views import RegistrarUsuario

# Ceci en clase utiliza las views como clases
urlpatterns = [
    path('/form', RegistrarUsuario.as_views(), name='registrarse'),
]

# TODO continuar con la clase 7/7 desde el minuto 29
