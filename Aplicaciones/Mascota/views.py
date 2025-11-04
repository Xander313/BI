from django.contrib import messages
from django.shortcuts import redirect, render

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


def guardarMascota(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        especie_id = request.POST["especie"]
        raza_id = request.POST.get("raza")
        sexo = request.POST["sexo"]
        fecha_nacimiento = request.POST.get("fecha_nacimiento")
        edad_aproximada = request.POST.get("edad_aproximada")
        peso_kg = request.POST.get("peso_kg")
        estado_salud = request.POST["estado_salud"]
        descripcion = request.POST.get("descripcion", "")
        vacunas_al_dia = True if request.POST.get("vacunas_al_dia") else False
        esterilizado = True if request.POST.get("esterilizado") else False
        fecha_ingreso = request.POST["fecha_ingreso"]
        ubicacion_refugio = request.POST.get("ubicacion_refugio", "")
        foto_perfil = request.FILES.get("foto_perfil")

        especie = Especie.objects.get(id=especie_id)

        raza = None
        if raza_id:
            raza = Raza.objects.get(id=raza_id)

        if fecha_nacimiento == "":
            fecha_nacimiento = None

        if edad_aproximada == "":
            edad_aproximada = None
        else:
            edad_aproximada = int(edad_aproximada)

        if peso_kg == "":
            peso_kg = None

        Mascota.objects.create(
            nombre=nombre,
            especie=especie,
            raza=raza,
            sexo=sexo,
            fecha_nacimiento=fecha_nacimiento,
            edad_aproximada=edad_aproximada,
            peso_kg=peso_kg,
            estado_salud=estado_salud,
            descripcion=descripcion,
            vacunas_al_dia=vacunas_al_dia,
            esterilizado=esterilizado,
            fecha_ingreso=fecha_ingreso,
            ubicacion_refugio=ubicacion_refugio,
            foto_perfil=foto_perfil,
        )

        messages.success(request, "Pet saved successfully")

    return redirect("indexMascota")
