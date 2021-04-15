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

""" 
@login_required
def CrearPilotoKart(request):
	if request.method == 'POST':
		form = PilotoKartForm(request.POST)
		if form.is_valid():
			x = form.save(commit=False)
			x.carrera_piloto = request.user
			x.fecha_inscripcion = datetime.datetime.now()
			x.save()
			return HttpResponseRedirect('/')
	else:
		form = PilotoKartForm()

	return render(request, 'piloto_kart/registrar_piloto_kart.html',{'form': form})

 """