# comentarios/forms.py

from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']  
        # Agregar aquí todos los campos que desees mostrar en el formulario
