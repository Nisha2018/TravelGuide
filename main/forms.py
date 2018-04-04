from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from django.core.validators import validate_email



class LoginForm(forms.Form):
	username = forms.CharField(label='User Name', max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())



class UserCreationForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'Enter username'}
		), required=True, max_length=50)

	email = forms.CharField(widget=forms.EmailInput(
		attrs={'class':'form-control','placeholder':'Enter email ID'}
		), required=True, max_length=50)

	first_name = forms.CharField(widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'Enter first name'}
		), required=True, max_length=50)

	last_name = forms.CharField(widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'Enter last name'}
		), required=True, max_length=50)

	password = forms.CharField(widget=forms.PasswordInput(
		attrs={'class':'form-control','placeholder':'Enter password'}
		), required=True, max_length=50)

	confirm_password = forms.CharField(widget=forms.PasswordInput(
		attrs={'class':'form-control','placeholder':'Confirm password'}
		), required=True, max_length=50)

	class Meta():
		model = User
		fields = ['username','email','first_name','last_name','password','confirm_password']


	def clean_username(self):
		user = self.cleaned_data['username']
		try:
			match = User.objects.get(username= user)
		except:
			return self.cleaned_data['username']
		raise forms.ValidationError("Username already exist")



	def clean_confirm_password(self):
		pas = self.cleaned_data['password']
		cpas = self.cleaned_data['confirm_password']
		MIN_LENGTH = 8
		if pas and cpas:
			if pas!= cpas:
				raise forms.ValidationError("password and confirm password not matched")
			else:
				if len(pas) < MIN_LENGTH:
					raise forms.ValidationError("Password should have atleast %d characters" %MIN_LENGTH)
				if pas.isdigit():
					raise forms.ValidationError("Password should not be all numeric")




class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label="Name")
    contact_email = forms.EmailField(required=True, label="Email")
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Message"
    )