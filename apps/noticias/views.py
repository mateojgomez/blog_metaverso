from django.shortcuts import render, redirect
from .forms import FormNoticia
from .models import Noticia

def noticia(request):
    noticias = noticias.objects.all()
    return render (request, 'agregar_noticias.html',{'noticias': noticias})

def AgregarNoticia(request):
    formulario = FormNoticia(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
    return render(request,'agregar_noticias.html',{'formulario': formulario})

def EditarNoticia(request,id_noticia):
    noticia = Noticia.objects.filter(id=id_noticia).first()
    form = FormNoticia(instance=noticia)
    return render(request,'editar_noticia.html',{"form":form,'noticia':noticia})
    
def EliminarNoticia(request,id):
    noticia = Noticia.objects.filter(id=id)
    noticia.delete()
    return redirect(to='administrar_noticias')   