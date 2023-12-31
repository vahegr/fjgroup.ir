# Generated by Django 4.2.4 on 2023-09-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0006_remove_project_structure_project_base_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='builder',
        ),
        migrations.RemoveField(
            model_name='project',
            name='competition',
        ),
        migrations.RemoveField(
            model_name='project',
            name='completion',
        ),
        migrations.RemoveField(
            model_name='project',
            name='gross_floor_area',
        ),
        migrations.RemoveField(
            model_name='project',
            name='persian_builder',
        ),
        migrations.RemoveField(
            model_name='project',
            name='persian_competition',
        ),
        migrations.RemoveField(
            model_name='project',
            name='persian_completion',
        ),
        migrations.RemoveField(
            model_name='project',
            name='persian_gross_floor_area',
        ),
        migrations.RemoveField(
            model_name='project',
            name='persian_planing',
        ),
        migrations.RemoveField(
            model_name='project',
            name='persian_project_management',
        ),
        migrations.RemoveField(
            model_name='project',
            name='persian_ranking',
        ),
        migrations.RemoveField(
            model_name='project',
            name='persian_start_of_construction',
        ),
        migrations.RemoveField(
            model_name='project',
            name='planing',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_management',
        ),
        migrations.RemoveField(
            model_name='project',
            name='ranking',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_of_construction',
        ),
        migrations.AddField(
            model_name='project',
            name='engineer',
            field=models.CharField(blank=True, max_length=300, verbose_name='مهندس'),
        ),
        migrations.AddField(
            model_name='project',
            name='persian_engineer',
            field=models.CharField(blank=True, max_length=300, verbose_name='مهندس(فارسی)'),
        ),
        migrations.AddField(
            model_name='project',
            name='persian_planning',
            field=models.CharField(blank=True, max_length=300, verbose_name='برنامه ریزی(فارسی)'),
        ),
        migrations.AddField(
            model_name='project',
            name='planning',
            field=models.CharField(blank=True, max_length=300, verbose_name='برنامه ریزی'),
        ),
    ]
