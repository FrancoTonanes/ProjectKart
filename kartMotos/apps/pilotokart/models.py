from django.db import models
from apps.carreraKarting.models import CarreraKarting


# Create your models here.

class PilotoKart(models.Model):
    
    OpcionCategoria = [
		('1', '125cc'),
        ('2', '150cc'),
        ('3', '300cc'),
        ('4', '350cc'),
        ('5', '400cc'),
        ('6', '500cc'),
        ('7', '700cc'),
        ('8', '710cc'),
        ('9', '800cc'),
    ]
    
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    dni = models.BigIntegerField()
    fecha_nacimiento = models.DateField('Fecha de Nacimiento(DD/MM/AAAA)',null=True)
    domicilio = models.CharField(max_length = 50)
    ciudad = models.CharField(max_length = 50)
    provincia = models.CharField(max_length = 50)
    email = models.EmailField()
    telefono = models.BigIntegerField(null = True,blank=True)
    numero_kart = models.BigIntegerField()
    categoria = models.CharField(max_length=1,choices= OpcionCategoria)
    carrera = models.ForeignKey(CarreraKarting, null=True, related_name = 'piloto_carrera', on_delete = models.SET_NULL)
    #fecha_inscripcion = models.DateField()


