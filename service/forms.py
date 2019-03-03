#from django import forms
import geocoder
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis import forms
from .models import Supply, Demand , DrugStock, Assignment


MB_KEY = "pk.eyJ1IjoicnNoYW5kaWx5YSIsImEiOiJjanNwbXZlZWYwejhkNDltbHZydGllNnFlIn0.qXMInf37QhkXyPsfqzSk-g"

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

	def __init__(self, user, *args, **kwargs):
		super(AssignmentForm, self).__init__(*args, **kwargs)
		if user.profile.temp_address:
			address = user.profile.temp_address
		else:
			address = user.profile.address
		g = geocoder.mapbox(address, key=MB_KEY)
		p = Point(g.latlng[0],g.latlng[0], srid=4326)
		supply = Supply.objects.annotate(distance=Distance('location', p)).order_by('distance')[0:]
		stock = DrugStock.objects.annotate(distance=Distance('location', p)).order_by('distance')[0:]
		su = [(q.id, q.address) for q in supply]
		st = [(q.id, q.address) for q in stock]
		self.fields['pick_point'] = forms.ChoiceField(choices=su)
		self.fields['drop_point'] = forms.ChoiceField(choices=st)
	


