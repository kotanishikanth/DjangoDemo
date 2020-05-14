from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # default - required=Ture

    # nested namespace for configurations
    class Meta: 
        model = User # targeted model

        # fields here are fields on the form
        fields = ['username', 'email', 'password1', 'password2']