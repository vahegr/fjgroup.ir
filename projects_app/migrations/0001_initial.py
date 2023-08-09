# Generated by Django 4.2.4 on 2023-08-09 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('persian_title', models.CharField(max_length=200, verbose_name='عنوان فارسی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان تولید')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('persian_title', models.CharField(max_length=200, verbose_name='عنوان (فارسی)')),
                ('description', models.CharField(max_length=1500, verbose_name='توضیحات')),
                ('persian_description', models.CharField(max_length=1500, verbose_name='توضیحات (فارسی)')),
                ('location', models.CharField(blank=True, max_length=300, verbose_name='مکان')),
                ('persian_location', models.CharField(blank=True, max_length=300, verbose_name='مکان(فارسی)')),
                ('builder', models.CharField(blank=True, max_length=300, verbose_name='سازنده')),
                ('persian_builder', models.CharField(blank=True, max_length=300, verbose_name='سازنده(فارسی)')),
                ('project_management', models.CharField(blank=True, max_length=300, verbose_name='مدیریت پروژه')),
                ('persian_project_management', models.CharField(blank=True, max_length=300, verbose_name='مدیریت پروژه(فارسی)')),
                ('competition', models.CharField(blank=True, max_length=300, verbose_name='رقابت')),
                ('persian_competition', models.CharField(blank=True, max_length=300, verbose_name='رقابت(فارسی)')),
                ('ranking', models.CharField(blank=True, max_length=300, verbose_name='رتبه بندی')),
                ('persian_ranking', models.CharField(blank=True, max_length=300, verbose_name='رتبه بندی(فارسی)')),
                ('planing', models.CharField(blank=True, max_length=300, verbose_name='تاریخ برنامه ریزی')),
                ('persian_planing', models.CharField(blank=True, max_length=300, verbose_name='تاریخ برنامه ریزی(فارسی)')),
                ('start_of_construction', models.CharField(blank=True, max_length=300, verbose_name='شروع ساخت و ساز')),
                ('persian_start_of_construction', models.CharField(blank=True, max_length=300, verbose_name='شروع ساخت و ساز(فارسی)')),
                ('completion', models.CharField(blank=True, max_length=300, verbose_name='تاریخ تکمیل')),
                ('persian_completion', models.CharField(blank=True, max_length=300, verbose_name='تاریخ تکمیل(فارسی)')),
                ('gross_floor_area', models.CharField(blank=True, max_length=300, verbose_name='مساحت طبقه ناخالص')),
                ('persian_gross_floor_area', models.CharField(blank=True, max_length=300, verbose_name='مساحت طبقه ناخالص(فارسی)')),
                ('project_team', models.TextField(blank=True, max_length=3000, verbose_name='تیم پروژه')),
                ('persian_project_team', models.TextField(blank=True, max_length=3000, verbose_name='تیم پروژه(فارسی)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان تولید')),
                ('category', models.ManyToManyField(to='projects_app.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'پروژه',
                'verbose_name_plural': 'پروژه ها',
            },
        ),
    ]
