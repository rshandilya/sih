from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SupplyForm 
from .forms import DemandForm, DrugStockerForm
from drugs.forms import DrugForm, DrugCategoryForm
from .models import Supply

# Create your views here.

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
		return render(request,'registration/login.html')
	else:
		if request.method == "POST":
			drug_sform = DrugStockerForm(request.POST)
			if drug_sform.is_valid():
				drug_sform.save()
			return render(request,'home/services.html')
		else:
			drug_sform = DrugStockerForm()
		return render(request,
			          'service/drug_stocker.html', 
			          {'drug_sform': drug_sform,
			           })



