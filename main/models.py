from django.db import models
from django.contrib.auth.models import User


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
    repl_name = models.CharField(max_length = 255, default = '')


    def has_taskforlesson(self):
        if self.taskforlesson:
            return True
        else:
            return False

    def __str__(self):
        return self.title


class TaskForLesson(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete = models.CASCADE)

    def __str__(self):
        return 'Задание урока ' + str(self.lesson)


class FileOfTask(models.Model):
    task = models.ForeignKey(TaskForLesson, on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    description = models.TextField(default = '')

    def __str__(self):
        return 'Файл {} к заданию {}'.format(str(self.name), str(self.task))


class Notification(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    is_viewed = models.BooleanField(default = False)

    def __str__(self):
        return "Уведомление '{}' пользователю {}".format(self.title, self.user)



class Vacansy(models.Model):
    title = models.CharField(max_length = 255)
    company = models.CharField(max_length = 255)
    date = models.DateField(auto_now = True)
    salary = models.CharField(max_length = 255)

    requirement_experience_set = [
        ('no', 'Не требуется / Не важно'),
        ('1-3', 'От 1 года до 3-х лет'),
        ('3-6', 'от 3-х лет до 6 лет'),
        ('6-10', 'от 6 лет до 10 лет'),
        ('10+', 'от 10 лет')
    ]
    requirement_experience = models.CharField(max_length = 255, choices=requirement_experience_set)

    work_mode_set = [
        ('full', 'Полный день'),
        ('part', 'Частичная занятость'),
        ('project', 'Проект/Разовая работа'),
        ('internship', 'Стажировка')
    ]
    work_mode = models.CharField(max_length = 255, choices = work_mode_set)

    description = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def short_description(self):
        return str(self.description)[:100]


class VacansyRequirement(models.Model):
    title = models.CharField(max_length = 255)
    vacansy = models.ForeignKey(Vacansy, on_delete = models.CASCADE)


class VacansyResponsibility(models.Model):
    title = models.CharField(max_length = 255)
    vacansy = models.ForeignKey(Vacansy, on_delete = models.CASCADE)