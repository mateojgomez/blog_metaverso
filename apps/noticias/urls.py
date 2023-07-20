from django.contrib import admin
from django.urls import path
from .views import agregar_noticias

urlpatterns = [
    path('administrar/noticias/agregar_noticias', agregar_noticias ,name='agregar_noticias'),
]

