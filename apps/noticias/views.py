from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormNoticia
from .models import Noticia
from django.views.generic import ListView, DetailView

#def noticia(request):
 #   noticias = noticias.objects.all()
   # return render (request, 'agregar_noticias.html',{'noticias': noticias})


class NoticiaListViewAdmin(ListView):
    model = Noticia
    template_name= " administrar_noticias.html "
    context_object_name = "noticias"



class NoticiaListView(ListView):
    model = Noticia
    template_name= " noticias/noticias.html "
    context_object_name = "noticias"


class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = "noticias/noticia_individual.html"
    context_object_name = "noticias"
    pk_url_kwarg = "id"
    queryset = Noticia.objects.all()

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

    
def EliminarNoticia(request,):
    id=request.GET.get("id",None)
    
    if id: 
        noticia = Noticia.objects.filter(id=id)
        noticia.delete()
    return redirect(to='administrar_noticias')   
        
        