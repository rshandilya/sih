#from django import forms
from django.contrib.gis import forms
from .models import Supply, Demand , DrugStock

class DrugStockForm(forms.ModelForm):
	class Meta:
		model = DrugStock
		fields = ['name','address','stocker_type']
	

class SupplyForm(forms.Form):
	address = forms.CharField(widget=forms.Textarea)
	


class DemandForm(forms.ModelForm):
	class Meta:
		model = Demand
		fields = '__all__'


class AddressForm(forms.Form):
	address = forms.CharField(widget=forms.Textarea)






