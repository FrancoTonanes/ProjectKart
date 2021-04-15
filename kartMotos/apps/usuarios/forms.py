#
from django import forms
from apps.usuarios.models import Usuario

class ModificarUsuario(forms.ModelForm):

	class Meta:
		model = Usuario
		fields = ['first_name','last_name','email','fecha_nacimiento']