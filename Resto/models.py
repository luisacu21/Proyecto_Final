from django.db import models
from django.contrib.auth.models import User




# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    DNI = models.CharField(unique=True, max_length=10, null=True, blank=True)
    telefono = models.CharField(max_length=15)


class Sucursal(models.Model):
    ARG = 'Buenos Aires Argentina'
    PER = 'Lima Peru'
    COL = 'Bogota Colombia'
    BRA = 'Sao Paulo Brasil'

    Seleccion_Sucursal = (
        (ARG, 'Buenos Aires Argentina'),
        (PER, 'Lima Peru'),
        (COL, 'Bogota Colombia'),
        (BRA, 'Sao Paulo Brasil')
    )

    Ciudad = models.CharField(max_length=30,choices=Seleccion_Sucursal,default=ARG)



class Reservacion(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} -- DNI: {self.DNI} -- Numero de Mesa: {self.numero_mesa} -- Invitados: {self.num_invitados} -- Fecha: {self.fecha_de_reservacion}"
    
    nombre= models.CharField(max_length=60)
    DNI= models.CharField(unique=True, max_length=10, null=True, blank=True)
    numero_mesa = models.IntegerField()
    num_invitados = models.IntegerField()
    fecha_de_reservacion = models.DateField()

class Avatar(models.Model):
   
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.usuario} - {self.imagen}"



