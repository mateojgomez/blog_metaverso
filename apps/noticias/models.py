from django.db import models
from django.utils import timezone

# Create your models here.


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
    #imagen = 
    
    
    
    class Meta:
        ordering = ('-fecha',)
        
    def __str__(self):
        return self.titulo