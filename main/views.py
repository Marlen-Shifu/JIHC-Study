from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, TemplateView

from django.contrib.auth import authenticate, login, logout

from django.core.exceptions import ValidationError

from user_profile.forms import *
from .models import *

from .checking_git import check


def home(request, login_form = LoginForm, registration_form = RegistrationForm):
    return render(request, 'new/main.html', {'login_form': login_form, 'registration_form': registration_form})


def category(request, category_id):
    category = Category.objects.get(pk = category_id)
    courses = Course.objects.filter(direction__category = category)

    return render(request, 'new/courses.html', {'courses': courses, 'login_form': LoginForm, 'registration_form': RegistrationForm})


def course(request, course_id):
    course = Course.objects.get(pk = course_id)
    lessons = Lesson.objects.filter(course = course)

    response = render(request, 'new/lessons.html', {'lessons': lessons, 'login_form': LoginForm, 'registration_form': RegistrationForm})

    try:
        user = User.objects.get(username = request.user)
        user.usercourses.add_last_course(course)
    except Exception as e:
        pass

    return response


def lesson(request, lesson_id):
    lesson = Lesson.objects.get(pk = lesson_id)

    return render(request, 'new/insidecourses.html', {'lesson': lesson, 'login_form': LoginForm, 'registration_form': RegistrationForm})


def check_repository(request):
    git_repository = request.GET.get('git')

    lesson_name = request.GET.get('ln')
    lesson = Lesson.objects.get(title = lesson_name)

    list_of_files =  []

    for file in lesson.taskforlesson.fileoftask_set.all():
        list_of_files += file.name

    in_files, not_files = check(git_repository, list_of_files )

    content_text = 'Мы проверили ваше задание к уроку {}.<br>Результаты:<br>'.format(lesson)

    for in_file in in_files:
        content_text += '{} - Успех<br>'.format(in_file)

    for not_file in not_files:
        content_text += '{} - Провал<br>'.format(not_file)

    notification = Notification.objects.create(user = request.user, 
                                                title = 'Проверка задания {}'.format(lesson.taskforlesson),
                                                content = content_text)

    notification.save()

    return redirect('notifications')


class NotificationListView(ListView):

    model = Notification
    template_name = 'new/notifications.html'

    def get_queryset(self):
        qs = super().get_queryset()
        user_notifications = qs.filter(user = self.request.user).order_by('-pk')
        return user_notifications


class NotificationDetailView(DetailView):

    model = Notification
    template_name = 'new/notification_view.html'

    def get_queryset(self):
        qs = super().get_queryset()
        obj = qs.get(pk = self.kwargs['pk'])
        obj.is_viewed = True
        obj.save()
        return qs


def repl_page(request, repl_name, lesson_pk):
    lesson = Lesson.objects.get(pk = lesson_pk)
    tasks = lesson.taskforlesson.fileoftask_set.all()
    return render(request, 'new/task_repl.html', {'repl_name': repl_name, 'tasks': tasks})


def search(request):
    search_text = request.GET.get('search_text')
    courses = Course.objects.filter(title__contains = search_text)
    if len(courses) >= 1:
        return render(request, 'new/courses.html', {'courses': courses, 'is_search': True, 'message': 'Резуальтат поиска', 'login_form': LoginForm, 'registration_form': RegistrationForm})
    else:
        return render(request, 'new/courses.html', {'is_search': True, 'message': 'Результатов не найдено', 'login_form': LoginForm, 'registration_form': RegistrationForm})
    


class CoursesListView(ListView):
    model = Course
    order_by = '-pk'
    template_name = 'new/courses_list.html'



def add_course_to_favorite(request):
    user = User.objects.get(username = request.GET.get('user'))
    course = Course.objects.get(pk = request.GET.get('course_pk'))

    user.usercourses.add_my_course(course)

    return JsonResponse({'status': '200'})


def logout_user(request):
    logout(request)
    return redirect('home')


class About(TemplateView):
    template_name = 'new/about-us.html'