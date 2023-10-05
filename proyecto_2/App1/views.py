from django.shortcuts import render
from App1.forms import *
from App1.models import Curso

from django.http import HttpResponse

def inicio(request):
    return render(request, "App1/base.html")

def cursos(request):
    return render(request, "App1/cursos.html")

def profesores(request):
    return HttpResponse("Vista profesores")

def estudiantes(request):
    return HttpResponse("Vista estudiantes")

def entregables(request):
    return HttpResponse("Vista entregables")
   
def cursoFormulario(request):
 
      if request.method == 'POST':
 
            miFormulario = CursoFormulario(request.POST ) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
                  curso.save()
                  return render(request, "App1/base.html")
      else:
            miFormulario = CursoFormulario()
 
      return render(request, "App1/cursoFormulario.html", {"miFormulario": miFormulario}) 

def mostrar(request):
    pass

def buscar(request):
    
    if request.method == 'POST':
         
            miFormulario = BusquedaCursos(request.POST ) 
            print(miFormulario)
 
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])
                return render(request, "App1/lista.html", {"cursos": cursos})
            else:
                print("\n\nERROR IS_VALID FALSE\n\n")
    else:
        miFormulario = BusquedaCursos()
 
    return render(request, "App1/cursoFormulario.html", {"miFormulario": miFormulario})