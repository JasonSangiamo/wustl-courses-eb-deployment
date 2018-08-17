# Generated by Django 2.0.5 on 2018-05-19 03:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=50)),
                ('department_abbreviation', models.CharField(max_length=10)),
                ('course_number', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('units', models.CharField(max_length=50)),
                ('lab', models.CharField(max_length=25)),
                ('nameID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SectionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=50)),
                ('start_time', models.CharField(max_length=20)),
                ('end_time', models.CharField(max_length=20)),
                ('days', models.CharField(max_length=20)),
                ('final', models.CharField(max_length=25)),
                ('semester', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=10)),
                ('course_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseInfo')),
                ('students', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]