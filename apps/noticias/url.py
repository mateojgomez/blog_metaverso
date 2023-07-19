from django.contrib import admin
from django.urls import path, include
from .views import Administrar_noticias_Form

urlpatterns = [
    path('administrar_noticias/', Administrar_noticias_Form.as_view(),name='administrar_noticias'),
]
