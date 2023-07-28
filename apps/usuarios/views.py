from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def registrarse(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige al usuario a la página de inicio de sesión después del registro
            return redirect('form')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registrarse.html', {'form': form})
