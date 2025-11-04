import os

from django.conf import settings
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

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


def editPet(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    especies = Especie.objects.all().order_by("nombre")
    razas = Raza.objects.all().order_by("nombre")
    context = {
        "mascota": mascota,
        "especies": especies,
        "razas": razas,
    }
    return render(request, "Mascota/editPet.html", context)


def updateMascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)

    if request.method == "POST":
        mascota.nombre = request.POST["nombre"]
        especie_id = request.POST["especie"]
        raza_id = request.POST.get("raza")
        mascota.sexo = request.POST["sexo"]

        fecha_nacimiento = request.POST.get("fecha_nacimiento")
        mascota.fecha_nacimiento = fecha_nacimiento if fecha_nacimiento else None

        edad_aproximada = request.POST.get("edad_aproximada")
        mascota.edad_aproximada = int(edad_aproximada) if edad_aproximada else None

        peso_kg = request.POST.get("peso_kg")
        mascota.peso_kg = peso_kg if peso_kg else None

        mascota.estado_salud = request.POST["estado_salud"]
        mascota.descripcion = request.POST.get("descripcion", "")
        mascota.vacunas_al_dia = True if request.POST.get("vacunas_al_dia") else False
        mascota.esterilizado = True if request.POST.get("esterilizado") else False
        mascota.fecha_ingreso = request.POST["fecha_ingreso"]
        mascota.ubicacion_refugio = request.POST.get("ubicacion_refugio", "")

        nueva_foto = request.FILES.get("foto_perfil")
        if nueva_foto:
            if mascota.foto_perfil:
                ruta_anterior = mascota.foto_perfil.path
                if os.path.exists(ruta_anterior):
                    os.remove(ruta_anterior)
            mascota.foto_perfil = nueva_foto

        mascota.especie = Especie.objects.get(id=especie_id)
        mascota.raza = Raza.objects.get(id=raza_id) if raza_id else None

        mascota.save()
        messages.success(request, "Pet updated successfully")

    return redirect("indexMascota")


def deleteMascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)

    try:
        mascota.delete()
        messages.success(request, "Pet deleted successfully")
    except ProtectedError:
        messages.error(
            request,
            "Cannot delete this pet while related records exist. Remove those references first.",
        )
    else:
        if mascota.foto_perfil:
            ruta_foto = mascota.foto_perfil.path
            if os.path.exists(ruta_foto):
                os.remove(ruta_foto)

    return redirect("indexMascota")
