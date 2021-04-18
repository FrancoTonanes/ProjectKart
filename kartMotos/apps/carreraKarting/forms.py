from django import forms
from .models import CarreraKarting


class CarreraKartingForm(forms.ModelForm):
	class Meta:
		model = CarreraKarting
		fields = '__all__'
		