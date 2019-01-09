from django.db import models

class Personas(models.Model):
    nombre = models.CharField(max_length=75)
    apellido = models.CharField(max_length=50)
    tipoDocumento = models.IntegerField()
    documento = models.CharField(max_length=8)
    email = models.EmailField()