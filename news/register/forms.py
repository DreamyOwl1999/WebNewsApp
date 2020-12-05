from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    dob =   forms.DateField()

    class Meta:
    	model = User
    	fields = ["username", "email", "dob", "password1", "password2"]
