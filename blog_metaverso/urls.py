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
from apps.noticias.views import NoticiaListView, NoticiaDetailView, NoticiaListViewAdmin


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('form/', form, name='form'),
    # path('registrarse/', registrarse, name='registrarse'),
    path('recuperar_contraseña/', recuperar_contraseña,
         name='recuperar_contraseña'),
    # Ceci incluye las paths de las apps
    path('noticias/', include('apps.noticias.urls')),
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


]
