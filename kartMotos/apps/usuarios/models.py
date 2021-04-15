from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
	#DNI = models.PositiveIntegerField(serialize = False, verbose_name = 'DNI', null=True)
#	fecha_nacimiento = models.DateField('Fecha de Nacimiento(DD/MM/AAAA)',null=True)
	email = models.EmailField('Email', unique=True, primary_key = True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	is_admin = models.BooleanField(default=False,null=False, blank=True)
	
	def __str__(self):
		return self.first_name + self.last_name

	
	
	
