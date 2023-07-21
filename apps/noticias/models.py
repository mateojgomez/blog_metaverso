from django.db import models
from django.utils import timezone
from apps.usuarios.models import Usuarios
# Create your models here.


#noticias
class Categoria(models.Model):
    nombre = models.CharField(max_length=30,null=False)
    def __str__(self):
        return self.nombre
    

class Noticia(models.Model):
    titulo = models.CharField(max_length=50,null=False)
    creador=models.ForeignKey(Usuarios,on_delete=models.SET_NULL, null=True )
    contenido = models.TextField(null=False)
    fecha = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,null=True,default='Sin categoria')
    #imagen = 
    
    
    class Meta:
        ordering = ('-fecha',)
        
    def __str__(self):
        return self.titulo