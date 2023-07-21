from django.db import models

# Create your models here.


#categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=30,null=False)
    def __str__(self):
        return self.nombre
    
#noticias
class Noticia(models.Model):
    titulo = models.CharField(max_length=50,verbose_name="Titulo",null=False)
    contenido = models.TextField(verbose_name="Contenido",null=False)
    fecha = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria,verbose_name="Categoria",on_delete=models.SET_NULL,null=True,default='Sin categoria')
    #imagen = 
    
    
    
    class Meta:
        ordering = ('-fecha',)
        
    def __str__(self):
        return self.titulo