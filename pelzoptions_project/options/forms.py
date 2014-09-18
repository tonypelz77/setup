from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	username = forms.CharField()
	email = forms.CharField()
	
	class Meta:
		model = User
		fields = ['username','email']