from django.db import models


class Persona(models.Model):


    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)

    numero_identificacion = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    correo_electronico = models.EmailField(blank=True)
    telefono_contacto = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=120, blank=True)
    ciudad = models.CharField(max_length=80, blank=True)
    ocupacion = models.CharField(max_length=120, blank=True)

    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
