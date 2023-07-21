from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Categoria, Noticia
#Ceci crea las Clases de vistas

class AgregarCategoria(CreateView):
    model= Categoria
    fields=['nombre']
    template_name='agregar_categoria.html'
    succes_url = reverse_lazy('inicio')


class AgregarNoticia(CreateView):
    model= Noticia
    fields=['titulo','creador','contenido','categoria']
    template_name='agregar_noticias.html'
    succes_url = reverse_lazy('inicio')



def agregar_noticias(request):
    template_name='agregar_noticias.html'
    return render(request,template_name)