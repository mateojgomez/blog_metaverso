from django.shortcuts import render
from apps.noticias.models import Noticia

def index(request):
    noticias = Noticia.objects.all()
    return render(request,'index.html',{'noticias':noticias})

def registrarse(request):
    return render(request, 'registrarse.html' )

def administrar_noticias(request):
    return render(request,'administrar_noticias.html')

def administrar_categorias(request):
    return render(request,'administrar_categorias.html')



