from django.shortcuts import render
from apps.noticias.models import Noticia
from apps.usuarios.models import Contacto


def index(request):
    templates_name = 'index.html'
    return render(request, templates_name)


def form(request):
    templates_name = 'form.html'
    return render(request, templates_name)


def administrar_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'administrar_noticias.html', {'noticias': noticias})


def administrar_categorias(request):
    return render(request, 'administrar_categorias.html')


def recuperar_contraseña(request):
    return render(request, 'recuperar_contraseña.html')


def nosotros(request):
    return render(request, 'nosotros.html')


def contacto(request):
    return render(request, 'contacto.html')
