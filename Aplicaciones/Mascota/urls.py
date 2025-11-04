from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="indexMascota"),
    path("newPet/", views.newPet, name="newPet"),
    path("guardarMascota/", views.guardarMascota, name="guardarMascota"),
    path("editPet/<int:mascota_id>/", views.editPet, name="editPet"),
    path("updateMascota/<int:mascota_id>/", views.updateMascota, name="updateMascota"),
]
