from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def registrarse(request):
    return render(request, 'registrarse.html' )

def administrar_noticias(request):
    return render(request,'administrar_noticias.html')

def administrar_categorias(request):
    return render(request,'administrar_categorias.html')



