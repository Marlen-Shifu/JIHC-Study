from django.contrib import admin
from .models import *


class FileOfTaskInline(admin.TabularInline):
    
    model = FileOfTask


class TaskForLessonInline(admin.ModelAdmin):

	inlines = [
		FileOfTaskInline,
    ]


admin.site.register(Category)

admin.site.register(Direction)

admin.site.register(Course)

admin.site.register(Lesson)

admin.site.register(TaskForLesson, TaskForLessonInline)

admin.site.register(Notification)