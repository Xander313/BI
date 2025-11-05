import os
from datetime import date
from django.conf import settings
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from Aplicaciones.Mascota.models import Mascota
from Aplicaciones.Persona.models import Persona
from .models import Adopcion

def index(request):
    adopciones = Adopcion.objects.select_related("mascota", "persona").all()
    # Agregar las listas de mascotas y personas para el modal
    mascotas = Mascota.objects.all().order_by("nombre")
    personas = Persona.objects.filter(activo=True).order_by("nombres")
    
    context = {
        "adopciones": adopciones,
        "mascotas": mascotas,  # Para el modal de edición
        "personas": personas,  # Para el modal de edición
    }
    return render(request, "adopcion.html", context)  

def nueva_adopcion(request):
    mascotas = Mascota.objects.filter(adoptantes__isnull=True).order_by("nombre")
    personas = Persona.objects.filter(activo=True).order_by("nombres")
    context = {
        "mascotas": mascotas,
        "personas": personas,
    }
    return render(request, "agregaradopcion.html", context)  

def guardar_adopcion(request):
    if request.method == "POST":
        mascota_id = request.POST.get("mascota")
        persona_id = request.POST.get("persona")
        estado = request.POST.get("estado", "Activo")
        fecha_resolucion = request.POST.get("fecha_resolucion")
        observaciones = request.POST.get("observaciones", "").strip()
        documento_adopcion = request.FILES.get("documento_adopcion")

        if not mascota_id or not persona_id:
            messages.error(request, "Please select both pet and person.")
            return redirect("nuevaAdopcion")

        try:
            mascota = Mascota.objects.get(id=mascota_id)
            persona = Persona.objects.get(id=persona_id)
        except (Mascota.DoesNotExist, Persona.DoesNotExist):
            messages.error(request, "Selected pet or person does not exist.")
            return redirect("nuevaAdopcion")

        if Adopcion.objects.filter(mascota=mascota, persona=persona).exists():
            messages.error(request, "This adoption process already exists for the selected pet and person.")
            return redirect("nuevaAdopcion")

        if fecha_resolucion == "":
            fecha_resolucion = None
        elif fecha_resolucion:
            try:
                fecha_resolucion = date.fromisoformat(fecha_resolucion)
            except ValueError:
                messages.error(request, "Invalid resolution date.")
                return redirect("nuevaAdopcion")

        Adopcion.objects.create(
            mascota=mascota,
            persona=persona,
            estado=estado,
            fecha_resolucion=fecha_resolucion,
            observaciones=observaciones,
            documento_adopcion=documento_adopcion,
        )

        messages.success(request, "Adoption process created successfully")

    return redirect("indexAdopcion")

def editar_adopcion(request, adopcion_id):
    adopcion = get_object_or_404(Adopcion, id=adopcion_id)
    mascotas = Mascota.objects.all().order_by("nombre")
    personas = Persona.objects.filter(activo=True).order_by("nombres")
    context = {
        "adopcion": adopcion,
        "mascotas": mascotas,
        "personas": personas,
    }
    return render(request, "agregaradopcion.html", context)

def actualizar_adopcion(request, adopcion_id):
    adopcion = get_object_or_404(Adopcion, id=adopcion_id)

    if request.method == "POST":
        mascota_id = request.POST.get("mascota")
        persona_id = request.POST.get("persona")
        estado = request.POST.get("estado")
        fecha_resolucion = request.POST.get("fecha_resolucion")
        observaciones = request.POST.get("observaciones", "").strip()
        documento_adopcion = request.FILES.get("documento_adopcion")

        try:
            mascota = Mascota.objects.get(id=mascota_id)
            persona = Persona.objects.get(id=persona_id)
        except (Mascota.DoesNotExist, Persona.DoesNotExist):
            messages.error(request, "Selected pet or person does not exist.")
            return redirect("editarAdopcion", adopcion_id=adopcion_id)

        if Adopcion.objects.filter(mascota=mascota, persona=persona).exclude(id=adopcion_id).exists():
            messages.error(request, "This adoption process already exists for another record.")
            return redirect("editarAdopcion", adopcion_id=adopcion_id)

        adopcion.mascota = mascota
        adopcion.persona = persona
        adopcion.estado = estado

        if fecha_resolucion == "":
            adopcion.fecha_resolucion = None
        elif fecha_resolucion:
            try:
                adopcion.fecha_resolucion = date.fromisoformat(fecha_resolucion)
            except ValueError:
                messages.error(request, "Invalid resolution date.")
                return redirect("editarAdopcion", adopcion_id=adopcion_id)

        adopcion.observaciones = observaciones

        if documento_adopcion:
            if adopcion.documento_adopcion:
                ruta_anterior = adopcion.documento_adopcion.path
                if os.path.exists(ruta_anterior):
                    os.remove(ruta_anterior)
            adopcion.documento_adopcion = documento_adopcion

        adopcion.save()
        messages.success(request, "Adoption process updated successfully")

    return redirect("indexAdopcion")

def eliminar_adopcion(request, adopcion_id):
    adopcion = get_object_or_404(Adopcion, id=adopcion_id)

    try:
        if adopcion.documento_adopcion:
            ruta_documento = adopcion.documento_adopcion.path
            if os.path.exists(ruta_documento):
                os.remove(ruta_documento)
        adopcion.delete()
        messages.success(request, "Adoption process deleted successfully")
    except ProtectedError:
        messages.error(
            request,
            "Cannot delete this adoption process while related records exist.",
        )

    return redirect("indexAdopcion")