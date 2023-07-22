from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from .views import index
from .views import registrarse
from .views import administrar_noticias
from .views import administrar_categorias
from apps.noticias.views import AgregarNoticia
#from .views import publicaciones







urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index , name='index'),
    path('registrarse/',registrarse, name='registrarse'),
    #Ceci incluye las paths de las apps
    path('noticias/', include('apps.noticias.urls')),
   # path('publicaciones/', publicaciones, name= 'publicaciones'),
    path('administrar/noticias',administrar_noticias,name='administrar_noticias'),
    path('administrar/categorias',administrar_categorias,name='administrar_categorias'),
    path('administrar/noticias/agregar_noticias', AgregarNoticia,name='agregar_noticias')
]
