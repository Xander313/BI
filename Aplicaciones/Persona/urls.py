urlpatterns=[
    path('inicioem',views.inicio,name='inicioem'),
    path('nuevoEmpleado',views.nuevoEmpleado),
    path('guardarEmpleado',views.guardarEmpleado),
    path('eliminarEmpleado/<id>',views.eliminarEmpleado),
    path('editarEmpleado/<id>',views.editarEmpleado),
    path('procesarEdicionEmpleado',views.procesarEdicionEmpleado),
]