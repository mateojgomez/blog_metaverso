from apps.noticias import views
from django.urls import path
from .views import AgregarNoticia

urlpatterns = [
    path('agregar_noticias', views.AgregarNoticia ,name='agregar_noticias'),
]

