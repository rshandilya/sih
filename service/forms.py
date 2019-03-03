#from django import forms
from django.contrib.gis import forms
from .models import Supply, Demand , DrugStock, Assignment


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


class AssignmentForm(forms.Form):
	pick_date = forms.DateField()
	drop_date = forms.DateField()

	def __init__(self,su, st, *args, **kwargs):
		super(AssignmentForm, self).__init__(*args, **kwargs)
		self.fields['pick_point'] = forms.ChoiceField(choices=su)
		self.fields['drop_point'] = forms.ChoiceField(choices=st)
	
