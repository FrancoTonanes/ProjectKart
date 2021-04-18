from django.db import models
# Create your models here.

class CarreraKarting(models.Model):

	OpcionPiloto = [
		('1', 'Moto'),
        ('2', 'Karting'),
    ]
	

	tipo_carrera = models.CharField(max_length=1,choices= OpcionPiloto)

	nombre = models.CharField(max_length = 50)
	fecha = models.DateField()
	lugar = models.CharField(max_length = 80)
	precio = models.BigIntegerField()

	def __str__(self):
		return f"Carrera: {self.nombre} - Fecha: {self.fecha} - Lugar: {self.lugar} - Precio: {self.precio}"

