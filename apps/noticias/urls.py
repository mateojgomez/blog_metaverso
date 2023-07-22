from apps.noticias import views
from django.urls import path


urlpatterns = [
    path('agregar_noticias', views.AgregarNoticia ,name='agregar_noticias'),
    path('administrar/noticias/eliminar_noticia/<int:id>/', views.EliminarNoticia,name='eliminar_noticia')
]

