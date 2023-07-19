from .models import Usuarios
from django.contrib.auth.forms import UserCreationForm


class Administrar_noticias_Form(UserCreationForm):
    
    class Meta:
        model = Noticias 
        fields = ['usuario','nombre','titulo', 'fecha_creacion','contenido','imagen']
        
  