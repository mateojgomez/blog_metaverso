from django.shortcuts import render, redirect
from .models import Comentario
from .forms import ComentarioForm

def crear_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre-de-la-vista-del-articulo')  # Redirige a la vista del artículo
    else:
        form = ComentarioForm()

    return render(request, 'crear_comentario.html', {'form': form})
# Create your views here.
