from django.db import models

class ServicioHotel(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion= models.CharField(blank=True, max_length=50)

    def __str__(self) -> str :
        return self.nombre

class Hotel(models.Model):
    precio_hotel = models.FloatField(blank=True, null=True)
    nombre = models.CharField(max_length=50)
    ubucacion = models.CharField(max_length=50)
    descripcion = models.CharField(blank=True, max_length=50,)
    servicio_hotel = models.ManyToManyField(ServicioHotel, null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre

class ServicioUnidad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(blank=True, max_length=50)

    def __str__(self) -> str:
        return self.nombre

class Unidad(models.Model):
    numero_unidad = models.IntegerField()
    piso = models.IntegerField()
    servicio_unidad = models.ManyToManyField(ServicioUnidad, null=True, blank=True)
    hotel = models.ForeignKey(Hotel, null=True, blank=True, on_delete=models.CASCADE)

    def __int__(self) -> int:
        return self.numero_unidad
  
