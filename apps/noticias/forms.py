from django import forms 
from .models import Noticia, Comentario

class FormNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
        
class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
