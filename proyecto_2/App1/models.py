from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()

class Sucursal(models.Model):
    calle = models.CharField(max_length=40)
    altura = models.IntegerField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    edad = models.IntegerField()