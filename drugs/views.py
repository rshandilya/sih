from django.shortcuts import render, redirect
from django.http import HttpResponse
from drugs.models import Drug
from drugs.models import DrugCategory , DrugStock
from .forms import DrugForm
from service.forms import SupplyForm
from django.urls import reverse
from service.models import Supply

# Create your views here.
def medicine(request):
	return render(request,'medicine/medicine.html')

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
			return redirect(reverse('home:home'))
		else:
			drug_form = DrugForm()
			supply_form = SupplyForm()
		return render(request,
			          'drugs/drug_donation.html', 
			          {'drug_form': drug_form,
			           'supply_form': supply_form})
