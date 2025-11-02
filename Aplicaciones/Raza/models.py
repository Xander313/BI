from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Raza(models.Model):

    nombre = models.CharField(max_length=80)
    descripcion = models.TextField(blank=True)
    temperamento_predominante = models.CharField(max_length=120, blank=True)

    esperanza_vida_media = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(40)],
        null=True,
        blank=True,
    )

    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    