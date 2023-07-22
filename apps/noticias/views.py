from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import FormNoticia

def noticia(request):
    noticias = noticias.objects.all()
    return render (request, 'agregar_noticias.html',{'noticias': noticias})

def AgregarNoticia(request):
    formulario = FormNoticia(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request,'agregar_noticias.html',{'formulario': formulario})
   