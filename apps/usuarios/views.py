from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import Usuarios
from .forms import RegistrarUsuariosForm
from apps.usuarios import forms


"""def registrarse(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige al usuario a la página de inicio de sesión después del registro
            return redirect('form')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registrarse.html', {'form': form})"""


class RegistrarUsuario(CreateView):
    model = Usuarios
    templates_name = 'templates/form.html'
    form_class = forms
    success_url = reversed_lazy('index')
