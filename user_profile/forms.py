from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from django import forms


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']

