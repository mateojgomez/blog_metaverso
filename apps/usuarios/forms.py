from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuarios


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuarios
        # Puedes agregar más campos aquí si es necesario
        fields = ['nombre', 'apellido',
                  'fecha_nacimiento', 'es_colaborador', 'imagen']
