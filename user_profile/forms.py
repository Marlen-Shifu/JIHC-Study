from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from django import forms

from .models import Profile


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'register_inputname'

    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'register_inputname'

    class Meta:
        model = User
        fields = ['username', 'email']


class ChangeProfilePhoto(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['photo']
