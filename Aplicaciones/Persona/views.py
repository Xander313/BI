

# Create your views here.
from .models import Persona
from django.shortcuts import render, redirect
from django.contrib import messages

def inicio(request):
    listadoPersona=Persona.objects.all()
    return render(request,"inicioper.html",{'empleado':listadoPersona})
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
            identificacion=identificacion,
            fecha_nacimiento=fecha_nacimiento,
            correo=correo,
            telefono=telefono,
            direccion=direccion,
            ciudad=ciudad,
            ocupacion=ocupacion,
        )
    #mensaje de confirmacion
    messages.success(request,"Persona guardado exitosamente")
    return redirect('inicioper')














