


from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='home'),
   	path('contacto',views.contacto,name='contacto'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('cuidados',views.cuidados, name='cuidados'),
    path('Login',auth.LoginView.as_view(template_name="usuarios/login.html"),name="login"),
    path('Logout',auth.LogoutView.as_view(),name="logout"),

    #Url de las apps
    path('usuarios/',include('apps.usuarios.urls')),
    path('carreraKarting/',include('apps.carreraKarting.urls')),
    path('pilotokart/',include('apps.pilotokart.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
