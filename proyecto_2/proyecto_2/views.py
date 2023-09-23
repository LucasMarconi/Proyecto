from django.template import loader
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo!")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a mi pagina.")

# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context

def probando_template(request):

    nombre = "Lucas"
    apellido = "Monteleone"
    diccionario = {"nombre": nombre, "apellido": apellido, 
                   "notas": [4, 8, 9, 10, 7, 8]}

    # Abrimos el archivo html
    mi_html = open('./proyecto_2/plantillas/index.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto en el que invocamos las variables para mandarlas al index
    mi_contexto = Context(diccionario)

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)

def usando_loader(request):
    
    nombre= "Micaela"
    apellido= "Gonzalez"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "notas": [7, 6, 9, 10, 7, 8]
    }
    plantilla = loader.get_template('index.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

from App1.models import Curso

def curso(request):
    curso = Curso(nombre="Desarrollo Web", camada="19881")
    curso.save()
    documento = f"Curso: {curso.nombre},  Camada: {curso.camada}"
    return HttpResponse(documento)