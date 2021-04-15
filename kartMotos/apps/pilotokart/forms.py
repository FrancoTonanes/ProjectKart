from django import forms
from .models import PilotoKart


class PilotoKartForm(forms.ModelForm):
	class Meta:
		model = PilotoKart
		fields = '__all__'
		