from django.contrib import admin
from .models import *


class FileOfTaskInline(admin.TabularInline):
    
    model = FileOfTask


class TaskForLessonInline(admin.ModelAdmin):

	inlines = [
		FileOfTaskInline,
    ]



class VacansyRequirementInline(admin.TabularInline):
    model = VacansyRequirement

class VacansyResponsibilityInline(admin.TabularInline):
    model = VacansyResponsibility

class VacansyAdmin(admin.ModelAdmin):

    inlines = [
        VacansyRequirementInline,
        VacansyResponsibilityInline
    ]


admin.site.register(Category)

admin.site.register(Direction)

admin.site.register(Course)

admin.site.register(Lesson)

admin.site.register(TaskForLesson, TaskForLessonInline)

admin.site.register(Notification)

admin.site.register(Vacansy, VacansyAdmin)