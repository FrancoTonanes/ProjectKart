#
from django.urls import reverse_lazy
from .models import Carrera
from django.shortcuts import render
from .forms import CarreraForm
from django.views.generic import CreateView

# Create your views here.
class RegistrarCarrera(CreateView):
	model = Carrera
	form_class = CarreraForm
	template_name = 'carreras/registrar_carrera.html'
	success_url = reverse_lazy('home')
