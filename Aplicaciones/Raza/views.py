from django.contrib import messages
from django.shortcuts import redirect

from .models import Raza


def guardar_raza(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        descripcion = request.POST.get("descripcion", "")
        temperamento_predominante = request.POST.get("temperamento_predominante", "")
        esperanza_vida_media = request.POST.get("esperanza_vida_media")

        Raza.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            temperamento_predominante=temperamento_predominante,
            esperanza_vida_media=esperanza_vida_media,
        )

        messages.success(request, "Breed saved successfully")

    return redirect("newPet")
