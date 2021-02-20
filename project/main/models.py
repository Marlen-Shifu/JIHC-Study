from django.db import models


class Category(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Direction(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to='static/photo/direction')
    description = models.TextField()

    def __str__(self):
        return self.title


class Course(models.Model):
    direction = models.ForeignKey(Direction, on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='static/photo/course')
    description = models.TextField()
    duration = models.CharField(max_length = 10)
    language = models.CharField(max_length = 15)
    author = models.CharField(max_length = 255)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=10)
    link = models.CharField(max_length = 355, default = '')

    def __str__(self):
        return self.title
