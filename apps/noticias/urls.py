from apps.noticias import views
from django.urls import path

app_name='noticias'

urlpatterns = [
    path('agregar_noticias', views.AgregarNoticia ,name='agregar_noticias'),
    path('administrar/noticias/eliminar_noticia/<int:id>/', views.EliminarNoticia,name='eliminar_noticia'),
    path('listar',views.NoticiaListView.as_view(), name = "noticias")
]

