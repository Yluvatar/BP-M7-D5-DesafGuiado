from django.db import models

# Create your models here.


class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20, blank=False, null=False)
    modelo = models.CharField(max_length=20, blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    activo = models.BooleanField(default=False, blank=False, null=False)


class RegistroContabilidad(models.Model):
    fecha_compra = models.DateField(blank=False, null=False)
    valor = models.FloatField(blank=False, null=False)
    vehiculo_id = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)


class Chofer(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    vehiculo_id = models.OneToOneField(Vehiculo, null=True, on_delete=models.CASCADE)