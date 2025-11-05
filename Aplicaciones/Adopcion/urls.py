from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="indexAdopcion"),
    path("nueva-adopcion/", views.nueva_adopcion, name="nuevaAdopcion"),
    path("guardar-adopcion/", views.guardar_adopcion, name="guardarAdopcion"),
    path("editar-adopcion/<int:adopcion_id>/", views.editar_adopcion, name="editarAdopcion"),
    path("actualizar-adopcion/<int:adopcion_id>/", views.actualizar_adopcion, name="actualizarAdopcion"),
    path("eliminar-adopcion/<int:adopcion_id>/", views.eliminar_adopcion, name="eliminarAdopcion"),
]