from .models import Usuarios
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate, login


class RegistroUsuarioForm(UserCreationForm):

    class Meta:
        model = Usuarios
        fields = ['username', 'nombre', 'apellido', 'email', 'imagen']
         
         


class ModificarPerfilForm(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = ['username', 'nombre', 'apellido', 'email', 'imagen']
    #password = forms.Charfield(max_length=200, required=True);
    #password_new = forms.CharField(max_length=200, required=True);
    
    
         
    



class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(request, username=username,password=password)
        if user:
            login(request, user)
