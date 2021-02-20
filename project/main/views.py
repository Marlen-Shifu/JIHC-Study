from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from django.core.exceptions import ValidationError

from .forms import *
from .models import *


def home(request, login_form = LoginForm, registration_form = RegistrationForm):
    return render(request, 'new/main.html', {'login_form': login_form, 'registration_form': registration_form})


def category(request, category_id):
    category = Category.objects.get(pk = category_id)
    direction = Direction.objects.get(category = category)
    courses = Course.objects.filter(direction = direction)

    return render(request, 'new/courses.html', {'courses': courses, 'login_form': LoginForm, 'registration_form': RegistrationForm})


def course(request, course_id):
    course = Course.objects.get(pk = course_id)
    lessons = Lesson.objects.filter(course = course)

    return render(request, 'new/lessons.html', {'lessons': lessons, 'login_form': LoginForm, 'registration_form': RegistrationForm})


def lesson(request, lesson_id):
    lesson = Lesson.objects.get(pk = lesson_id)

    return render(request, 'new/insidecourses.html', {'lesson': lesson, 'login_form': LoginForm, 'registration_form': RegistrationForm})


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
