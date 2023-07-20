from django.shortcuts import render


def agregar_noticias(request):
    template_name='agregar_noticias.html'
    return render(request,template_name)