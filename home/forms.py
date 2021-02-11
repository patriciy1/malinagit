from django import forms
from .models import ShippingAddress

class StatusForm(forms.ModelForm):
	class Meta:
		model = ShippingAddress
		fields = ['status',]

