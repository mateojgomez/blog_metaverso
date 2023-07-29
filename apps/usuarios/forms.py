from .models import Usuarios
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


class RegistrarUsuariosForm(UserCreationForm):
    class Meta:
        model = Usuarios
        # Puedes agregar más campos aquí si es necesario
        fields = ['nombre', 'apellido',
                  'fecha_nacimiento', 'es_colaborador', 'imagen']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_superuser = False
        user.is_staff = False
        user.save()
        return user
