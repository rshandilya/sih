#from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
import geocoder


MAPBOX_KEY = "pk.eyJ1IjoicnNoYW5kaWx5YSIsImEiOiJjanNwbXZlZWYwejhkNDltbHZydGllNnFlIn0.qXMInf37QhkXyPsfqzSk-g"

# Create your models here.
class Demand(models.Model):
	recipient = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.TextField(max_length=100)
	request_on = models.DateField(auto_now_add=True)
	received_on = models.DateField(null=True, blank=True)	
	location = models.PointField(null=True, blank=True)
	
	def save(self, *args, **kwargs):
		g = geocoder.mapbox(self.address, key=MAPBOX_KEY)
		self.location = Point(g.latlng)
		super(Demand, self).save(*args, **kwargs)

class Supply(models.Model):
	donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='med_donations')
	address = models.TextField(max_length=100)
	donated_on = models.DateField(auto_now_add=True)
	location = models.PointField(null=True, blank=True)

	def save(self, *args, **kwargs):
		g = geocoder.mapbox(self.address, key=MAPBOX_KEY)
		self.location = Point(g.latlng)
		super(Supply, self).save(*args, **kwargs)

	
class DrugStock(models.Model):

	STYPE = (
		('H','Hospital'),
		('P','Pharmacy'),
		)

	name=models.CharField(max_length=30)
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	address = models.TextField(blank=True,null=True)
	stocker_type = models.CharField(default=0,max_length=2,choices=STYPE)
	location = models.PointField(null=True, blank=True) 
	
	def save(self, *args, **kwargs):
		g = geocoder.mapbox(self.address, key=MAPBOX_KEY)
		self.location = Point(g.latlng)
		super(DrugStock, self).save(*args, **kwargs)


class Assignment(models.Model):
	transporter = models.ForeignKey(User, on_delete=models.CASCADE)
	source = models.OneToOneField(Supply, on_delete=models.CASCADE)
	dest = models.OneToOneField(DrugStock, on_delete=models.CASCADE)
	pick_date = models.DateField()
	drop_date = models.DateField()

	