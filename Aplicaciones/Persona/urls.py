from django.urls import path
from . import views

urlpatterns=[
    path('inicioper',views.inicio,name='inicioper'),
    path('nuevapersona',views.nuevapersona),
    path('guardarPersona',views.guardarPersona),
    path('eliminarPersona/<id>',views.eliminarPersona),
    path('editarPersona/<id>',views.editarPersona),
    path('procesarEdicionPersona',views.procesarEdicionPersona),
]