

# Create your views here.
from datetime import datetime
from .models import Persona
from django.shortcuts import render, redirect
from django.contrib import messages

def inicio(request):
    listadoPersona=Persona.objects.all()
    return render(request,"inicioper.html",{'persona':listadoPersona})
def nuevapersona(request):
    return render(request,"nuevapersona.html")
def guardarPersona(request):
    nombres = request.POST["nombres"]
    apellidos = request.POST["apellidos"]
    identificacion = request.POST["identificacion"]
    fecha_nacimiento = request.POST["fecha_nacimiento"]
    correo = request.POST["correo"]
    telefono = request.POST["telefono"]
    direccion = request.POST["direccion"]
    ciudad = request.POST["ciudad"]
    ocupacion = request.POST["ocupacion"]
    nuevapersona=Persona.objects.create(
            nombres=nombres,
            apellidos=apellidos,
            numero_identificacion=identificacion,
            fecha_nacimiento=fecha_nacimiento,
            correo_electronico=correo,
            telefono_contacto=telefono,
            direccion=direccion,
            ciudad=ciudad,
            ocupacion=ocupacion,
        )
    #mensaje de confirmacion
    messages.success(request,"Person saved successfully")
    return redirect('inicioper')


def eliminarPersona(request,id):
    personaEliminar = Persona.objects.get(id=id)
    personaEliminar.delete()
    messages.success(request,"Person successfully removed")
    return redirect('inicioper')

#editar
def editarPersona(request,id):
    personaEditar=Persona.objects.get(id=id)
    return render(request,"editarPersona.html",{'personaEditar':personaEditar})

def procesarEdicionPersona(request):
    id = request.POST["id"]
    persona = Persona.objects.get(id=id)

    persona.nombres = request.POST["nombres"]
    persona.apellidos = request.POST["apellidos"]
    persona.numero_identificacion = request.POST["identificacion"]

    fecha_nacimiento = request.POST["fecha_nacimiento"]
    if fecha_nacimiento:
        persona.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
    else:
        persona.fecha_nacimiento = None

    persona.correo_electronico = request.POST["correo"]
    persona.telefono_contacto = request.POST["telefono"]
    persona.direccion = request.POST["direccion"]
    persona.ciudad = request.POST["ciudad"]
    persona.ocupacion = request.POST["ocupacion"]

    persona.save()
    messages.success(request, "Successfully updated person")
    return redirect('inicioper')











