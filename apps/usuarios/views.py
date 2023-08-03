from .forms import RegistroUsuarioForm, ModificarPerfilForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from apps.usuarios.models import Usuarios
from .forms import ContactoForm


class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        messages.success(
            self.request, 'Registro exitoso. Por favor, inicia sesión')
        form.save()

        return redirect('index')


def ModificarPerfil(request, id):
    usuario = get_object_or_404(Usuarios, id=id)

    data = {
        'form': ModificarPerfilForm(instance=usuario)
    }

    if request.method == 'POST':
        formulario = ModificarPerfilForm(
            data=request.POST, instance=usuario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
        data["form"] = formulario

    return render(request, 'modificar_perfil.html', data)


class LoginUsuario(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        messages.success(self.request, '')
     # TODO no redirige
        return reverse('index')


class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'

    def get_success_url(self):
        messages.success(self.request, '')
# TODO
        return reverse('index')


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'contacto.html')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})
