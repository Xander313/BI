

# Create your views here.
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
    messages.success(request,"Persona guardada exitosamente")
    return redirect('inicioper')


def eliminarPersona(request,id):
    personaEliminar = Persona.objects.get(id=id)
    personaEliminar.delete()
    messages.success(request,"Persona ELIMINADO exitosamente")
    return redirect('inicioper')

#editar
def editarPersona(request,id):
    personaEditar=Persona.objects.get(id=id)
    return render(request,"editarPersona.html",{'personaEditar':personaEditar})

def procesarEdicionPersona(request):
    id=request.POST["id"]
    nombres = request.POST["nombres"]
    apellidos = request.POST["apellidos"]
    identificacion = request.POST["identificacion"]
    fecha_nacimiento = request.POST["fecha_nacimiento"]
    correo = request.POST["correo"]
    telefono = request.POST["telefono"]
    direccion = request.POST["direccion"]
    ciudad = request.POST["ciudad"]
    ocupacion = request.POST["ocupacion"]
    
    
    persona=Persona.objects.get(id=id)
    persona.nombres=nombres,
    persona.apellidos=apellidos,
    persona.identificacion=identificacion,
    persona.fecha_nacimiento=fecha_nacimiento,
    persona.correo=correo,
    persona.telefono=telefono,
    persona.direccion=direccion,
    persona.ciudad=ciudad,
    persona.ocupacion=ocupacion,
    persona.save()
    messages.success(request,"Persona ACTUALIZADO exitosamente")
    return redirect('inicioper')











