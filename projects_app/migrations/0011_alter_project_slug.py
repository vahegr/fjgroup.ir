# Generated by Django 4.2.4 on 2023-09-09 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0010_alter_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True),
        ),
    ]
