from django.shortcuts import render
from App1.forms import *
from App1.models import Cliente
from django.http import HttpResponse

def inicio(request):
    return render(request, "App1/base.html")

def clientes(request):
    return render(request, "App1/clientes.html")

def productos(request):
    return HttpResponse("Vista estudiantes")

def sucursales(request):
    return HttpResponse("Vista entregables")
   
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

def mostrar(request):
    pass

def buscar(request):
    
    if request.method == 'POST':
         
            miFormulario = BusquedaClinete(request.POST ) 
            print(miFormulario)
 
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                clientes = Cliente.objects.filter(nombre__icontains=informacion["nombre"])
                return render(request, "App1/lista.html", {"clientes": clientes})
            else:
                print("\n\nERROR IS_VALID FALSE\n\n")
    else:
        miFormulario = BusquedaClinete()
 
    return render(request, "App1/clienteFormulario.html", {"miFormulario": miFormulario})