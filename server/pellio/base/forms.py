from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    FirstName = forms.CharField(
        required = True,
        label = 'FirstName',
        max_length = 32,
    )
    LastName = forms.CharField(
        required = True,
        label = 'FirstName',
        max_length = 32, 
    )
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
		required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

