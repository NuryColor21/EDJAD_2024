from django.db import models

# Create your models here.

class reporte (models.Model):
    id_usuario = models.CharField (max_length=5)
    description = models.CharField (max_length=30)
    ubicacion = models.CharField (max_length=100)
    imagen = models.ImageField (upload_to= '')
    fecha = models.DateField(("Fecha"), auto_now=True, auto_now_add=False)
    hora = models.TimeField(("Hora"))

class Usuario(models.Model):
    id_usuario = models.CharField(max_length=50)
    id_rol = models.IntegerField()
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

class RolLevel(models.Model):
    id_rol = models.IntegerField()
    name = models.CharField(max_length=40)
    
class Permisos(models.Model):
    nombre = models.CharField(max_length=10)

