from django.urls import path
from App1 import views

urlpatterns = [
    path('inicio/', views.inicio),
    path('cursos/', views.cursos, name="cursos"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('entregables/', views.entregables, name="Entregables"),
    path('cursoform/', views.cursoFormulario, name="CursoForm"),
    path('buscarform/', views.buscar, name="Buscar"),
    path('mostrarform/', views.mostrar, name="Mostrar"),
]