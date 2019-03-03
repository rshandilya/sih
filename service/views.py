from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SupplyForm
from .forms import DemandForm, DrugStockForm, AddressForm
from drugs.forms import DrugForm, DrugCategoryForm
from .models import Supply, DrugStock
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
import geocoder

# Create your views here.

MB_KEY = "pk.eyJ1IjoicnNoYW5kaWx5YSIsImEiOiJjanNwbXZlZWYwejhkNDltbHZydGllNnFlIn0.qXMInf37QhkXyPsfqzSk-g"

def service(request):
	return render(request,'home/services.html')

def donate_medicine(request):
	if not request.user.is_authenticated:
		return redirect(reverse('login'))
	else:
		if request.method == "POST":
			drug_form = DrugForm(request.POST)
			supply_form = SupplyForm(request.POST)
			if drug_form.is_valid() and supply_form.is_valid():
				supply = Supply.objects.create(donor=request.user,
					                  address=supply_form.cleaned_data['address'])
				drug_form.save(commit=False)
				drug_form.instance.supply = supply
				drug_form.save()			
			return redirect(reverse('account:donations'))
		else:
			drug_form = DrugForm()
			supply_form = SupplyForm()
		return render(request,
			          'service/drug_donation.html', 
			          {'drug_form': drug_form,
			           'supply_form': supply_form})


def drug_stock(request):
	if not request.user.is_authenticated:
		return redirect(reverse('login'))
	else:
		if request.method == "POST":
			stock_form = DrugStockForm(request.POST)
			if stock_form.is_valid():
				stock_form.save(commit=False)
				stock_form.instance.user = request.user
				stock_form.save()
				request.user.is_stocker = True
				request.user.save()
			return redirect(reverse('account:profile'))
		else:
			stock_form = DrugStockForm()
		return render(request,
			          'service/drug_stock.html', 
			          {'stock_form': stock_form})


def check_assignment(request):
	if request.method == 'POST':
		form = AddressForm(request.POST)
		if form.is_valid():
			address = form.cleaned_data['address']		
			g = geocoder.mapbox(address, key=MB_KEY)
			p = Point(g.latlng[0],g.latlng[0], srid=4326)
			supply = Supply.objects.annotate(distance=Distance('location', p)).order_by('distance')[0:]
			stock = DrugStock.objects.annotate(distance=Distance('location', p)).order_by('distance')[0:]
			context = {'supply': supply, 'stock': stock, 'form': form}
			return render(request, 'service/check_assignment.html', context )
	else:
		form = AddressForm()
		context = {'form': form}
	return render(request, 'service/check_assignment.html', context )
	




