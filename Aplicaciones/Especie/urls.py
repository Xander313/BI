from django.urls import path

from . import views

urlpatterns = [
    path("guardarEspecie/", views.guardar_especie, name="guardarEspecie"),
]
