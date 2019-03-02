from django.shortcuts import render

# Create your views here.
def services(request):
	return render(request,'home/services.html')

def support_us(request):
	return render(request,'home/support_us.html')
