from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('profile/', profile, name='profile'),
    path('category/<int:category_id>/', category, name='category'),
    path('course/<int:course_id>/', course, name='course'),
    path('lesson/<int:lesson_id>/', lesson, name='lesson'),
]
