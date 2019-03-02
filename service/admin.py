from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import Supply, Demand

# Register your models here.
#admin.site.register(Supply)
admin.site.register(Demand)



@admin.register(Supply)
class SupplyAdmin(OSMGeoAdmin):
    list_display = ('address', 'location')