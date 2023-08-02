from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Usuarios(AbstractUser):
    # contraseña = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    # fecha_nacimiento = models.DateField('Fecha_nacimiento',null=True,auto_now_add=True)
    es_colaborador = models.BooleanField('Es_colaborador', default=False)
    imagen = models.ImageField(
        null=True, blank=True, upload_to='usuarios', default='usuarios/usuario_def.png')
    # Sugerencia de chatgpt para resolver conflictos
    # app_label = 'usuarios'
    # groups = models.ManyToManyField(
    #   'auth.Group', blank=True, related_name='user_groups')
    # user_permissions = models.ManyToManyField(
    #   'auth.Permission', blank=True, related_name='user_permissions')

    def get_absolute_url(self):
        return reverse("index")

    # def __str__(self):
      #  return self.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
