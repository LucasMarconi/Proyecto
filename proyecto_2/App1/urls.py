from django.urls import path
from App1 import views

urlpatterns = [
    path('inicio/', views.inicio),
    path('cursos/', views.cursos, name="cursos"),
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('entregables/', views.entregables)
]