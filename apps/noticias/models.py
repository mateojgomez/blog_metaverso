from django.db import models
from usuarios.models import Usuarios
# Create your models here.

class Noticias(models.Model):
    
    usuario = models.ForeignKey(Usuarios)
    titulo = models.CharField(max_length=20)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField(max_length=6000)
    imagen = models.ImageField(null=True, blank=True, upload_to='media/noticias',default='static/img/usuario_def.png')
    
    def __str__(self):
        return self.titulo
    
    