from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_mascota'),
    path('/newPet', views.newPet, name="newPetUrl"),

]
