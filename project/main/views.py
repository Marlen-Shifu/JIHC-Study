from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from django.core.exceptions import ValidationError

from user_profile.forms import *
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