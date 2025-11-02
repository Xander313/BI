from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Mascota(models.Model):


    nombre = models.CharField(max_length=80)
    especie = models.ForeignKey(
        "Especie.Especie",
        on_delete=models.PROTECT,
        related_name="mascotas",
    )
    raza = models.ForeignKey(
        "Raza.Raza",
        on_delete=models.PROTECT,
        related_name="mascotas",
        null=True,
        blank=True,
    )
    sexo = models.CharField(max_length=6,)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    edad_aproximada = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(25)],
        help_text="Edad estimada en años cuando no existe fecha de nacimiento exacta.",
        null=True,
        blank=True,
    )
    peso_kg = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
    )
    estado_salud = models.CharField(max_length=12)
    descripcion = models.TextField(blank=True)
    vacunas_al_dia = models.BooleanField(default=False)
    esterilizado = models.BooleanField(default=False)
    fecha_ingreso = models.DateField()

    ubicacion_refugio = models.CharField(
        max_length=120,
        blank=True,
    )
    foto_perfil = models.ImageField(upload_to="mascotas/", null=True, blank=True)

    adoptantes = models.ManyToManyField(
        "Persona.Persona",
        through="Adopcion.Adopcion",
        related_name="mascotas",
        blank=True,
    )