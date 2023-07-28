from django.contrib import admin
from django.urls import path
from . import views

# Ceci en clase utiliza las views como clases
urlpatterns = [
    path('registrarse/', views.registrarse, name='registrarse'),
]

# TODO continuar con la clase 7/7 desde el minuto 29
