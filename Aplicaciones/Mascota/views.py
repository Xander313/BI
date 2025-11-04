from django.shortcuts import render

from Aplicaciones.Especie.models import Especie
from Aplicaciones.Raza.models import Raza

from .models import Mascota


def index(request):
    mascotas = Mascota.objects.select_related("especie", "raza").all()
    context = {
        "mascotas": mascotas,
    }
    return render(request, "Mascota/index.html", context)


def newPet(request):
    especies = Especie.objects.all().order_by("nombre")
    razas = Raza.objects.all().order_by("nombre")
    context = {
        "especies": especies,
        "razas": razas,
    }
    return render(request, "Mascota/newPet.html", context)
