# Generated by Django 4.2.4 on 2023-09-08 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0007_remove_project_builder_remove_project_competition_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-created_at',), 'verbose_name': 'پروژه', 'verbose_name_plural': 'پروژه ها'},
        ),
    ]