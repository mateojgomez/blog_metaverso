from django.db import models
from django.utils import timezone
from django.conf import settings
from apps.usuarios.models import Usuarios

#categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=30,null=False)
    def __str__(self):
        return self.nombre
    
#noticias
class Noticia(models.Model):
    titulo = models.CharField(max_length=50,null=False)
    contenido = models.TextField(null=False)
    fecha = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria,verbose_name="Categoria",on_delete=models.SET_NULL,null=True,default='Sin categoria')
    imagen = models.ImageField(null=False, blank=True, upload_to='noticias', default='noticias/noticia-default.png')

    
    
    class Meta:
        ordering = ('-fecha',)
        
    def __str__(self):
        return self.titulo
    
    
class Comentario(models.Model):
    posts = models.ForeignKey('noticias.Noticia', on_delete=models.CASCADE,related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.texto


