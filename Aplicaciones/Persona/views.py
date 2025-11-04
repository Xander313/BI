

# Create your views here.
from .models import Persona
from django.shortcuts import render, redirect
from django.contrib import messages

def inicio(request):
    listadoPersona=Persona.objects.all()
    return render(request,"inicioper.html",{'empleado':listadoPersona})
def nuevoEmpleado(request):
    return render(request,"nuevoEmpleado.html")
#Almacenando los datos de cargo en la Bdd
