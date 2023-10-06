from django.urls import path
from App1 import views

urlpatterns = [
    path('inicio/', views.inicio),
    path('clientes/', views.clienteFormulario, name="Clientes"),
    path('productos/', views.productos, name="Productos"),
    path('sucursales/', views.sucursales, name="Sucursales"),
    path('buscarform/', views.buscar, name="Buscar"),
    path('mostrarform/', views.mostrar, name="Mostrar"),
]