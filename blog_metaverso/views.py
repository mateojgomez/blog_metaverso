from django.shortcuts import render
from apps.noticias.models import Noticia


def index(request):
    return render(request, 'index.html')


def registrarse(request):
    return render(request, 'registrarse.html')


def administrar_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'administrar_noticias.html', {'noticias': noticias})


def administrar_categorias(request):
    return render(request, 'administrar_categorias.html')


def form(request):
    return render(request, 'form.html')


def recuperar_contraseña(request):
    return render(request, 'recuperar_contraseña.html')

# def publicaciones(request):
 #   noticias = Noticia.objects.all()
  #  return render(request,'publicaciones.html',{'noticias':noticias})
