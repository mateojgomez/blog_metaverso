from django import forms 
from .models import Noticia

class FormNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
