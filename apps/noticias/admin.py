from django.contrib import admin
from .models import Categoria, Noticia

# Register your models here.
@admin.register(Noticia)
class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','contenido','fecha','categoria')
    
    
admin.site.register(Categoria)