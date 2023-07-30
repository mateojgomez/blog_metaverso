from apps.noticias import views
from django.urls import path
from apps.noticias.views import EliminarNoticia, ComentarioCreateView
from blog_metaverso.views import administrar_noticias


app_name='noticias'

urlpatterns = [
    path('',views.NoticiaListView.as_view(), name = "noticias"),
    path('<int:id>/comentarios',ComentarioCreateView.as_view(), name = "comentarios"),
    path('administrar/', administrar_noticias,name='administrar_noticias'),
    path('agregar_noticias', views.AgregarNoticia ,name='agregar_noticias'),
    path('noticias/administrar/eliminar_noticia/<int:id>/', EliminarNoticia,name='eliminar_noticia'),
    path('comentarios/',ComentarioCreateView.as_view(), name = "comentarios"),
    #path('eliminar_noticia/', EliminarNoticia,name='eliminar_noticia'),
]

