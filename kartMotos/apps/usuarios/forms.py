#
from django import forms
from .models import Usuario
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm

""" 

class ModificarUsuario(forms.ModelForm):

	class Meta:
		model = Usuario
		fields = ['first_name','last_name','email','fecha_nacimiento'] """



class UsuarioForm(UserCreationForm):


	class Meta:
		model = Usuario 
		fields = ['first_name','last_name','email','password1','password2']
""" 
	@transaction.atomic
	def save(self):
		usuario = super().save(commit = False)
		usuario.save()
		Usuario.objects.create(usuario=usuario)
		return usuario """


