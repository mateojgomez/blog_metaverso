from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormNoticia, FormComentario
from .models import Noticia, Comentario, Categoria
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

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
    
    def get_queryset(self):
        categoria_seleccionada = self.request.GET.get('categoria')
        fecha_orden = self.request.GET.get('fecha_orden')
        orden_alfabetico = self.request.GET.get('orden_alfabetico')
        
        noticias = Noticia.objects.all()
        
        if categoria_seleccionada:
            categoria = get_object_or_404(Categoria, nombre=categoria_seleccionada)
            noticias = Noticia.objects.filter(categoria=categoria)


        if fecha_orden == 'ascendente':
            noticias = noticias.order_by('fecha')
        elif fecha_orden == 'descendente':
            noticias = noticias.order_by('-fecha')
            
        if orden_alfabetico == 'ascendente':
            noticias = noticias.order_by('titulo')
        elif orden_alfabetico == 'descendente':
            noticias = noticias.order_by('-titulo')


        return noticias
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        return context
    
    


class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = "noticias/noticia_individual.html"
    context_object_name = "noticias"
    pk_url_kwarg = "id"
    queryset = Noticia.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FormComentario()
        context['comentarios'] = Comentario.objects.filter(posts_id=self.kwargs['id'])
        return context
    
    def post(self,request,*args,**kwargs):
        form = FormComentario(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            
            comentario.posts_id = self.kwargs['id']
            comentario.save()
            return redirect('noticia_individual', id=self.kwargs['id'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
        


class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormComentario
    template_name = 'comentario/agregar_comentario.html'
    succes_url = 'comentario/comentarios/'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.posts_id = self.kwargs['posts_id']
        return super().form_valid(form)
    



def EditarComentario(request, id):
    comentario = get_object_or_404(Comentario, id=id)
    data = {'form': FormComentario(instance=comentario)}
   
    if request.method == 'POST':
        formulario = FormComentario(data=request.POST, instance=comentario)
        if formulario.is_valid():
            formulario.save()
            
            noticia_id = comentario.posts.id
            
            return redirect(reverse('noticia_individual', kwargs={'id': noticia_id}))
        data["form"] = formulario
        
    return render(request, 'editar_noticia.html', data)




def AgregarNoticia(request):
    data = {
        'form': FormNoticia()
    }
    
    formulario = FormNoticia(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect(to= '/administrar/noticias')
    return render(request,'agregar_noticias.html',{'formulario': formulario})

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


def EliminarComentario(request,id):
    comentario = get_object_or_404(Comentario, id=id)
    id_post = comentario.posts.id
    comentario.delete()
    return redirect('/noticias/' + str(id_post))