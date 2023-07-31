from django.db import models
from apps.noticias.models import Noticia
from apps.usuarios.models import Usuarios

class Comentario(models.Model):
    contenido = models.TextField()
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE,  related_name='comentarios_noticia')
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='comentarios_usuario')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario {self.id}'

