from django.urls import path
from . import views

app_name = 'drugs'
urlpatterns = [
    path('',views.medicine,name='medicine'),
    path('donate',views.donate_medicine, name='donate_medicine'),
]
