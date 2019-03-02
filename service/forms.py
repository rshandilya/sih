#from django import forms
from django.contrib.gis import forms
from .models import Supply, Demand , DrugStock

class DrugStockerForm(forms.ModelForm):
	class Meta:
		model = DrugStock
		fields = ['stocker_type','name','address',]
	

class SupplyForm(forms.Form):
	address = forms.CharField(widget=forms.Textarea)
	


class DemandForm(forms.ModelForm):
	class Meta:
		model = Demand
		fields = '__all__'

