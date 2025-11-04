from django.urls import path

from . import views

urlpatterns = [
    path("guardarRaza/", views.guardar_raza, name="guardarRaza"),
]
