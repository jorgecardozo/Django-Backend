from django.db import models

class Perro(models.Model):
    nombre = models.CharField(max_length=75)
    apellido = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()