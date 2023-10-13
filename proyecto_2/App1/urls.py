from django.urls import path
from App1 import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('clientes/', views.clienteFormulario, name="Clientes"),
    path('productos/', views.productosFormulario, name="Productos"),
    path('sucursales/', views.sucursalesFormulario, name="Sucursales"),
    path('buscarform/', views.buscarCli, name="Buscar"),
    path('borrarprod/<int:prod_id>/', views.borrarproducto, name="BorrarProd"),
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name='Register'),

]

#Vistas basadas en clases
urlpatterns += [
    path('logout/', LogoutView.as_view(template_name='App1/base.html'), name='Logout'),
    path('clases/listas/', views.ClienteListView.as_view(), name='List'),
    path('clases/nuevo/', views.ClienteCreateView.as_view(), name='New'),
    path('clases/eliminar/<int:pk>/', views.ProdDeleteView.as_view(), name='Delete'),
    path('clases/editar/<int:pk>/', views.ClienteUpdateView.as_view(), name='Edit'),
    path('clases/detalle/<int:pk>/', views.ProdDetalleView.as_view(), name='Detail'),
]