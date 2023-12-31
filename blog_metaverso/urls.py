from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from .views import index
from .views import form
# from .views import registrarse
from .views import recuperar_contraseña
from .views import administrar_noticias
from .views import administrar_categorias
from apps.noticias.views import AgregarNoticia, EliminarNoticia, EditarNoticia
from apps.noticias.views import NoticiaListView, NoticiaDetailView, NoticiaListViewAdmin, ComentarioCreateView
from apps.noticias.models import Comentario
from apps.usuarios.views import LogoutUsuario
from .views import nosotros
from . import views


urlpatterns = [
    path('', NoticiaListView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('index/', NoticiaListView.as_view(), name='index'),
    path('usuarios/', include('apps.usuarios.urls')),
    path('noticias/', include('apps.noticias.urls', namespace='noticias')),


    # Ceci incluye las paths de las apps

    path('administrar/noticias', administrar_noticias,
         name='administrar_noticias'),
    path('administrar/categorias', administrar_categorias,
         name='administrar_categorias'),
    path('administrar/noticias/agregar_noticias',
         AgregarNoticia, name='agregar_noticias'),
    path('administrar/noticias/eliminar_noticia/',
         EliminarNoticia, name='eliminar_noticia'),
    path('administrar/noticias/editar_noticia/<int:id>/',
         EditarNoticia, name='editar_noticia'),
    path('noticias/<int:id>/', NoticiaDetailView.as_view(),
         name="noticia_individual"),
    path('', include('django.contrib.auth.urls')),
    path('nosotros/', nosotros, name='nosotros'),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
