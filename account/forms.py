from django import forms
from .models import User 
from .models import Profile # CHANGE
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

#class CustomUserCreationForm(UserCreationForm):
#	class Meta:
#		model = User
#		fields = UserCreationForm.Meta.fields

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = User
		fields = ['first_name','last_name','username','email',] 
		

class ProfileForm(forms.ModelForm):     # CHANGE
	class Meta:
		model = Profile                 # CHANGE
		fields = ['address','phone',]



		
		
