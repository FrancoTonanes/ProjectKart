#
from django.contrib import admin
from django.urls import path
from . import views

app_name="usuarios"

urlpatterns = [

	#path('Modificar/<str:pk>', views.Modificar.as_view(), name="modificar"),

    path('RegistrarUsuario/',views.RegistroUsuario.as_view(), name = "registrar_usuario"),

]