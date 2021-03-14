from django.db import models
from django.contrib.auth.models import User
from main.models import Course


class UserCourses(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	last_courses = models.ManyToManyField(Course, related_name = 'last_courses', blank = True)
	my_courses = models.ManyToManyField(Course, related_name = 'my_courses', blank = True)

	def __str__(self):
		return 'Курсы ' + str(self.user)


	def add_last_course(self, course):
		if self.last_courses.count() == 4:
			self.last_courses.remove(self.last_courses.all().order_by('-pk').last())
			

		if course not in self.last_courses.all():
			self.last_courses.add(course)


	def add_my_course(self, course):
		if course not in self.my_courses.all():
			self.my_courses.add(course)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to = 'users/', blank=True)