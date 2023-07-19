from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Noticias
from .forms import Administrar_noticias_Form

# Create your views here.

class RegistrarUsuario(CreateView):
    model = Noticias
    template_name = 'administrar_noticias.html'
    form_class = Administrar_noticias_Form
    success_url = reverse_lazy('inicio')
    
