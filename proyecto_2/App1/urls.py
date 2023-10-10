from django.urls import path
from App1 import views

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('clientes/', views.clienteFormulario, name="Clientes"),
    path('productos/', views.productosFormulario, name="Productos"),
    path('sucursales/', views.sucursalesFormulario, name="Sucursales"),
    path('buscarform/', views.buscarCli, name="Buscar"),
]