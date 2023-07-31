from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse,reverse_lazy


class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        messages.success(
            self.request, 'Registro exitoso. Por favor, inicia sesión')
        form.save()

        return redirect('index')


class LoginUsuario(LoginView):
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        messages.success(self.request,'Login exitoso')
     #TODO no redirige   
        return reverse('index')
    
class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'

    def get_success_url(self):
        messages.success(self.request, 'Logout exitoso')
#TODO
        return reverse('index')
