from django.db import models
from django.contrib.auth.models import User
from service.models import Supply, Demand, DrugStock
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
	

class Drug(models.Model):	
	name = models.CharField(max_length=30,null=True)
	composition = models.CharField(max_length=30)
	quantity = models.PositiveIntegerField(null=True, blank=True)
	exp_date = models.DateField(help_text="dd/mm/yyyy",null=True,blank=True)
	#description = models.TextField(blank=True,null=True
	supply = models.ForeignKey(Supply,on_delete=models.CASCADE,null=True,blank=True)
	demand = models.ForeignKey(Demand,on_delete=models.CASCADE,null=True,blank=True)
	drug_stock = models.ForeignKey(DrugStock,on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		return self.name


class DrugCategory(models.Model):
	
	ROUTE = (
        ('I', 'Injection'),
        ('O', 'Oral'),
        ('T', 'Tablet'),
        ('S', 'Syrup'),
        ('C', 'Cream'),
        ('L', 'Liquid'),
        )

	NATURE = (
		('D','Depressants'),
		('S','Stimulants'),
		('H','Hallucinogens'),
		('O','Opioids'),
		('I','Inhalants'),
		('C','Cannabis'),

		)

	DISEASE = (
		('D','Digestive_system'),
		('B','Body_pain'),
		('E','Eye'),
		('S','Skin'),
		('A','Alergy'),
		('F','Fever'),
		('CL','Cold'),
		('C','Cough'),
		('D','Diabetes'),
		('R','Respiratory_System'),
		('V','Vitamins'),
		('EN','Ear,Nose,oropharynx'),
		('O','Other'),
		)

	AVAILABILITY = (
		('P','prescription_drug'),
		('NP','On_the_counter_medicine'),
		) 

	CATEGORY = (
		('G','Generic'),
		('B','Branded'),
		('E','Expired'),
		)
	
	drug = models.OneToOneField(Drug, 
		                        on_delete=models.CASCADE, 
		                        related_name='category')
	route = models.CharField(max_length=1, 
		                     choices=ROUTE, 
		                     null=True, 
		                     blank=True)
	nature = models.CharField(max_length=1, 
		                      choices=NATURE, 
		                      null=True, 
		                      blank=True)
	disease = models.CharField(max_length=2, 
		                       choices=DISEASE, 
		                       null=True, 
		                       blank=True)
	availability = models.CharField(max_length=2, 
		                            choices=AVAILABILITY,
		                            null=True, 
		                            blank=True)

	def __str__(self):
		return f"{self.drug} Category"


@receiver(post_save, sender=Drug)
def create_drug_category(sender, instance, created, **kwargs):
	if created:
		DrugCategory.objects.create(drug=instance)
	instance.category.save()

