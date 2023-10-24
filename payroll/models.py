from django.db import models

# Create your models here.
class Empleado(models.Model):
    ci = models.IntegerField(max_length=10, unique=True, verbose_name= "C.I.")
    name = models.CharField(max_length=75, verbose_name="Apellidos y Nombres")
    position = models.CharField(max_length=50, verbose_name="Cargo")
    pay = models.IntegerField(verbose_name="Sueldo")
    comissions = models.IntegerField(verbose_name="Comisiones")

    def __str__(self):
        fila = "C.I.: "+ str(self.ci) + " Nombre: "+ self.name
        return fila