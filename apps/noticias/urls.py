from django.contrib import admin
from django.urls import path
from .views import agregar_noticias , AgregarCategoria, AgregarNoticia
#Ceci en clase utiliza las views como clases
urlpatterns = [
    path('agregar_noticia', AgregarNoticia.as_view() ,name='agregar_noticia'),
    path('agregar_categoria', AgregarCategoria.as_view() ,name='agregar_categoria'),
]

#TODO continuar con la clase 7/7 desde el minuto 29