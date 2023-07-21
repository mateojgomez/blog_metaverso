from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuarios(AbstractUser):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField('Fecha_nacimiento')
    es_colaborador = models.BooleanField('Es_colaborador', default=False)
    imagen = models.ImageField(null=True, blank=True, upload_to='usuarios',default='usuarios/usuario_def.png')
    #Sugerencia de chatgpt para resolver conflictos
    app_label = 'usuarios'
    groups = models.ManyToManyField('auth.Group', blank=True, related_name='user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', blank=True, related_name='user_permissions')
    
    def __str__(self):
        return self.nombre

    