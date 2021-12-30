from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):  # remade UserCreationForm for Register Page
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
