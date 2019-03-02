from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm 
from .forms import ProfileForm , CustomUserChangeForm   # CHANGE
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Profile                          # CHANGE
from service.models import Supply

# Create your views here.

def sign_up(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect(reverse('account:profile'))
	else:
		form = UserCreationForm()
	return render(request,"account/sign_up.html", {'form':form})


def profile(request):
	return render(request, 'account/profile.html')

def edit_profile(request,id):
	if request.method == 'POST':
		user_form = CustomUserChangeForm(request.POST, instance=request.user)
		contact_form = ProfileForm(request.POST ,instance=request.user.profile) # CHANGE
		user_form.save(commit=False)
		contact_form.instance.user = request.user
		user_form.save()
		contact_form.save()
		#edit_form2.instance.user= edit_form.user
		#edit_form2 = edit_form2.save()
		return redirect(reverse('account:profile'))
			
	else:
		user_form = CustomUserChangeForm(instance=request.user)
		contact_form = ProfileForm(instance=request.user.profile)   # CHANGE
	return render(request, 
		          'account/edit_profile.html', 
		         {'user_form':user_form,
		          'contact_form':contact_form})


def donation_list(request):
	sup = Supply.objects.filter(donor=request.user)
	return render(request, 
		          'account/donation_list.html',
		          {'supply': sup})