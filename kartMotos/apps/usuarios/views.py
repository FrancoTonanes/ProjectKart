#
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
#from .forms import ModificarUsuario
from .models import Usuario
from django.shortcuts import render
from .forms import UsuarioForm
from django.views.generic import CreateView

""" 
class Modificar(UpdateView):
	model = Usuario
	form_class = ModificarUsuario
	template_name = 'usuarios/modificarUsuario.html'
	success_url = reverse_lazy('home') """


# Create your views here.
class RegistroUsuario(CreateView):
	model = Usuario
	form_class = UsuarioForm
	template_name = 'usuarios/registro_usuario.html'
	success_url = reverse_lazy('home')
