#
from django.urls import reverse_lazy
from .models import CarreraKarting
from django.shortcuts import render
from .forms import CarreraKartingForm
from django.views.generic import CreateView

# Create your views here.
class RegistrarCarreraKarting(CreateView):
	model = CarreraKarting
	form_class = CarreraKartingForm
	template_name = 'carreras/registrar_carrera.html'
	success_url = reverse_lazy('home')
