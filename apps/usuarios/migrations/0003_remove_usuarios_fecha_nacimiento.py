# Generated by Django 4.2.3 on 2023-07-30 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuarios_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='fecha_nacimiento',
        ),
    ]
