from django.core.validators import FileExtensionValidator
from django.db import models


class Adopcion(models.Model):

    mascota = models.ForeignKey(
        "Mascota.Mascota",
        on_delete=models.PROTECT,
        related_name="adopciones",
    )
    persona = models.ForeignKey(
        "Persona.Persona",
        on_delete=models.PROTECT,
        related_name="adopciones",
    )
    estado = models.CharField(
        max_length=15,
    )
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_resolucion = models.DateField(null=True, blank=True)
    observaciones = models.TextField(blank=True)
    documento_adopcion = models.FileField(
        upload_to="adopciones/",
        validators=[FileExtensionValidator(["pdf"])],
        blank=True,
        null=True
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-fecha_solicitud"]
        verbose_name = "Proceso de adopcion"
        verbose_name_plural = "Procesos de adopcion"
        constraints = [
            models.UniqueConstraint(
                fields=["mascota", "persona"],
                name="unique_mascota_persona_en_adopcion",
            )
        ]

    def __str__(self) -> str:
        return f"{self.mascota} - {self.persona} ({self.estado})"
