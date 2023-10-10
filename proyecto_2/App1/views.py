from django.shortcuts import render
from App1.forms import *
from App1.models import *

def inicio(request):
    clientes = Cliente.objects.all()
    suc = Sucursal.objects.all()
    prod = Producto.objects.all()
    return render(request, "App1/base.html", {"clientes": clientes, "sucursales": suc, "productos": prod})

def productosFormulario(request):
    
    if request.method == 'POST':
 
            miFormulario = ProductoFormulario(request.POST ) 
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  prod = Producto(nombre=informacion['nombre'], precio=informacion['precio'])
                  prod.save()
                  return render(request, "App1/base.html")
    else:
            miFormulario = ProductoFormulario()
 
    return render(request, "App1/ProductoFormulario.html", {"miFormulario": miFormulario})

def sucursalesFormulario(request):
    
    if request.method == 'POST':
 
            miFormulario = SucursalFormulario(request.POST ) 
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  suc = Sucursal(calle=informacion['calle'], altura=informacion['altura'])
                  suc.save()
                  return render(request, "App1/base.html")
    else:
            miFormulario = SucursalFormulario()
 
    return render(request, "App1/SucursalFormulario.html", {"miFormulario": miFormulario})
   
def clienteFormulario(request):
 
      if request.method == 'POST':
 
            miFormulario = ClienteFormulario(request.POST ) 
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  cliente = Cliente(nombre=informacion['nombre'], email=informacion['email'],   edad=informacion['edad'])
                  cliente.save()
                  return render(request, "App1/base.html")
      else:
            miFormulario = ClienteFormulario()
 
      return render(request, "App1/clienteFormulario.html", {"miFormulario": miFormulario}) 

def buscarCli(request):
    
    if request.method == 'POST':
         
            miFormulario = BusquedaCliente(request.POST ) 
            print(miFormulario)
 
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                clientes = Cliente.objects.filter(nombre__icontains=informacion["nombre"])
                return render(request, "App1/lista.html", {"clientes": clientes})
            else:
                print("\n\nERROR IS_VALID FALSE\n\n")
    else:
        miFormulario = BusquedaCliente()
 
    return render(request, "App1/clienteFormulario.html", {"miFormulario": miFormulario})