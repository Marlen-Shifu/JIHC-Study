from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('courses/', CoursesListView.as_view(), name='courses'),
    path('category/<int:category_id>/', category, name='category'),
    path('course/<int:course_id>/', course, name='course'),
    path('lesson/<int:lesson_id>/', lesson, name='lesson'),
    path('check/', check_repository, name='check'),
    path('notifications/', NotificationListView.as_view(), name='notifications'),
    path('notifications/<int:pk>/', NotificationDetailView.as_view(), name='notification'),
    path('repl/<str:repl_name>/<int:lesson_pk>/', repl_page, name='repl'),
    path('search/', search, name='search'),
    path('add_course_to_favorite/', add_course_to_favorite, name = 'add_course_to_favorite'),
    path('logout/', logout_user, name = 'logout'),
]
