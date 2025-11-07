from django.db.models import Avg, Count, DurationField, ExpressionWrapper, F
from django.db.models.functions import TruncMonth
from django.shortcuts import render

from Aplicaciones.Adopcion.models import Adopcion


def dashboard(request):
    top_species_qs = (
        Adopcion.objects.values("mascota__especie__nombre")
        .annotate(total=Count("id"))
        .order_by("-total")[:5]
    )

    top_breeds_qs = (
        Adopcion.objects.exclude(mascota__raza__isnull=True)
        .values("mascota__raza__nombre")
        .annotate(total=Count("id"))
        .order_by("-total")[:5]
    )

    top_person_qs = (
        Adopcion.objects.values(
            "persona__nombres",
            "persona__apellidos",
        )
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    species_chart = {
        "labels": [item["mascota__especie__nombre"] for item in top_species_qs],
        "counts": [item["total"] for item in top_species_qs],
    }

    breeds_chart = {
        "labels": [item["mascota__raza__nombre"] for item in top_breeds_qs],
        "counts": [item["total"] for item in top_breeds_qs],
    }

    top_person = None
    if top_person_qs:
        first = top_person_qs[0]
        full_name = f'{first["persona__nombres"]} {first["persona__apellidos"]}'.strip()
        top_person = {
            "name": full_name or "Sin nombre",
            "count": first["total"],
        }

    avg_resolution_delta = (
        Adopcion.objects.filter(fecha_resolucion__isnull=False)
        .aggregate(
            promedio=Avg(
                ExpressionWrapper(
                    F("fecha_resolucion") - F("fecha_solicitud"),
                    output_field=DurationField(),
                )
            )
        )
        .get("promedio")
    )

    avg_resolution_days = None
    if avg_resolution_delta:
        avg_resolution_days = round(avg_resolution_delta.total_seconds() / 86400, 1)

    avg_duration_chart = {
        "average": avg_resolution_days,
        "target": 30,  # meta de referencia en días
    }

    status_qs = (
        Adopcion.objects.values("estado")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    status_chart = {
        "labels": [item["estado"] or "Sin estado" for item in status_qs],
        "counts": [item["total"] for item in status_qs],
    }

    monthly_qs = (
        Adopcion.objects.annotate(month=TruncMonth("fecha_solicitud"))
        .values("month")
        .annotate(total=Count("id"))
        .order_by("-month")[:6]
    )

    monthly_list = list(monthly_qs)[::-1]

    monthly_chart = {
        "labels": [
            item["month"].strftime("%b %Y") if item["month"] else "Sin fecha"
            for item in monthly_list
        ],
        "counts": [item["total"] for item in monthly_list],
    }

    context = {
        "species_chart": species_chart,
        "breeds_chart": breeds_chart,
        "top_person": top_person,
        "avg_adoption_days": avg_resolution_days,
        "avg_duration_chart": avg_duration_chart,
        "status_chart": status_chart,
        "monthly_chart": monthly_chart,
    }

    return render(request, "Resportes/index.html", context)
