from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from django.core.exceptions import ValidationError

from .forms import *
from .models import *

from main.views import home


def profile(request):

    user = User.objects.get(username = request.user)

    return render(request, 'new/user.html', {'user': user, 'photo_change_form': ChangeProfilePhoto})


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
            return render(request, 'new/log in.html', {'login_form': form})
    else:
        return render(request, 'new/log in.html', {'login_form': LoginForm})


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            user = form.save()           
            user_courses = UserCourses(user = user)
            user_courses.save()
            profile = Profile(user = user)
            profile.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'new/register.html', {'registration_form': form})
    else:
        return render(request, 'new/register.html', {'registration_form': RegistrationForm})


def change_user_photo(request):
    if request.method == 'POST':
        form = ChangeProfilePhoto(request.POST, request.FILES)
        if form.is_valid():

            try:
                profile = Profile.objects.get(user=request.user)
                profile.photo = form.cleaned_data['photo']
                profile.save()
            except:
                profile = Profile(user = request.user, photo=form.cleaned_data['photo'])  
                profile.save()

            return render(request, 'new/user.html', {'photo_change_form': ChangeProfilePhoto})