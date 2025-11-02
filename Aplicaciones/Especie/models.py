from django.db import models


class Especie(models.Model):

    nombre = models.CharField(max_length=60, unique=True)
    nombre_cientifico = models.CharField(max_length=120, blank=True)
    descripcion_general = models.TextField(blank=True)
    cuidados_recomendados = models.TextField(blank=True)

    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

