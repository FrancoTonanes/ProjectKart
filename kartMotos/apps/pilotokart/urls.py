from django.urls import path
from . import views

app_name = 'pilotokart'

urlpatterns = [
    path('registrarPilotoKart/',views.RegistrarPilotoKart.as_view(), name = "registrar_piloto_kart"),
    
]