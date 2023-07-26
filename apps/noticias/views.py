from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormNoticia
from .models import Noticia

def noticia(request):
    noticias = noticias.objects.all()
    return render (request, 'agregar_noticias.html',{'noticias': noticias})

def AgregarNoticia(request):
    data = {
        'form': FormNoticia()
    }
    
    formulario = FormNoticia(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request,'agregar_noticias.html',data)

def EditarNoticia(request,id):
    noticia = get_object_or_404(Noticia, id=id)
    
    data = {
        'form':FormNoticia(instance=noticia)
    }
   
    if request.method == 'POST':
        formulario = FormNoticia(data=request.POST, instance=noticia, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='administrar_noticias')
        data["form"]= formulario
        
    return render(request,'editar_noticia.html', data)

    
def EliminarNoticia(request,id):
    noticia = Noticia.objects.filter(id=id)
    noticia.delete()
    return redirect(to='administrar_noticias')   