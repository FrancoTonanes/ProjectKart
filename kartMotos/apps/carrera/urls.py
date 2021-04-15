from django.urls import path
from . import views

app_name = 'carrera'

urlpatterns = [
    path('registrarCarrera/',views.RegistrarCarrera.as_view(), name = "registrar_carrera"),
    
]