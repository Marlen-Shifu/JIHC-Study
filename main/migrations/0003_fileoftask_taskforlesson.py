# Generated by Django 3.1.5 on 2021-02-22 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_lesson_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskForLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='FileOfTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.taskforlesson')),
            ],
        ),
    ]