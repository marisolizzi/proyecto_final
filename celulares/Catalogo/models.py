from django.db import models

# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    detalle = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to="marcas",null=True,max_length=100)

class Celular(models.Model):
    nombre = models.CharField(max_length=50)
    detalle = models.CharField(max_length=1000)
    categoria = models.IntegerField()
    imagen = models.ImageField(upload_to="celulares",null=True,max_length=100)
