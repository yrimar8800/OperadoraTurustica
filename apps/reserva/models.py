from django.db import models

class Reserva(models.Model):
    fecha_ingreso = models.CharField(max_length=20)
    fecha_salida = models.CharField(max_length=20)
    cantidad_personas = models.IntegerField()