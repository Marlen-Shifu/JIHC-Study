from django.urls import path
from .views import *

urlpatterns = [
    path('', profile, name='profile'),
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('changephoto/', change_user_photo, name='change_photo'),
]
