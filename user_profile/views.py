from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from django.core.exceptions import ValidationError

from .forms import *


def profile(request):

    return render(request, 'new/user.html', {'login_form': LoginForm, 'registration_form': RegistrationForm})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    raise ValidationError('Account is not active.')
            else:
                raise ValidationError('Account is not register.')
        else:
            return home(request, login_form = form, registration_form = RegistrationForm)
    else:
        return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User(username = cd['username'], email = cd['email'], password = cd['password1'])
            user.save()
            login(request, user)
            return redirect('home')

        else:
            return home(request, login_form = LoginForm, registration_form = form)
    else:
        return redirect('home')