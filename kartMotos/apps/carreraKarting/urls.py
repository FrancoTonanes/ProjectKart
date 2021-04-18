from django.urls import path
from . import views

app_name = 'carrera_karting'

urlpatterns = [
    path('registrarCarreraKarting/',views.RegistrarCarreraKarting.as_view(), name = "registrar_carrera"),
    
]