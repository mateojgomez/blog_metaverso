from django.urls import path
from . import views

app_name='comentarios'

urlpatterns = [
    # Otras rutas de la aplicación comentarios, si las tienes
    path('crear/', views.crear_comentario, name='crear_comentario'),
]