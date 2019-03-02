from django import forms
from .models import Drug, DrugCategory 


class DrugForm(forms.ModelForm):
	class Meta:
		model = Drug
		exclude = ['price','category','supply','demand','drug_stock',]


class DrugCategoryForm(forms.ModelForm):
	class Meta:
		model = DrugCategory
		fields = ['route','disease']