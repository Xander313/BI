from django.contrib import messages
from django.shortcuts import redirect

from .models import Especie


def guardar_especie(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        nombre_cientifico = request.POST.get("nombre_cientifico", "")
        descripcion_general = request.POST.get("descripcion_general", "")
        cuidados_recomendados = request.POST.get("cuidados_recomendados", "")
        activo = True if request.POST.get("activo") else False

        Especie.objects.create(
            nombre=nombre,
            nombre_cientifico=nombre_cientifico,
            descripcion_general=descripcion_general,
            cuidados_recomendados=cuidados_recomendados,
            activo=activo,
        )

        messages.success(request, "Species saved successfully")

    return redirect(request.POST.get("next") or "newPet")
