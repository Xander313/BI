from django.shortcuts import render

from .models import Mascota


def index(request):
    mascotas = Mascota.objects.select_related("especie", "raza").all()
    context = {
        "mascotas": mascotas,
    }
    return render(request, "Mascota/index.html", context)
def newPet(request):

    return render(request, "Mascota/newPet.html")