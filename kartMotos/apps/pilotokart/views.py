from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import PilotoKart
from .forms import *



# Create your views here.
class RegistrarPilotoKart(CreateView):
	model = PilotoKart
	form_class = PilotoKartForm
	template_name = 'piloto_kart/registrar_piloto_kart.html'
	success_url = reverse_lazy('home')

def ListarInscripciones(request):
	context = {}
	todos = PilotoKart.objects.all()
	context['pilotos'] = todos
	return render(request,'piloto_kart/listar_inscripciones.html',context)
