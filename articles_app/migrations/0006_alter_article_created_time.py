# Generated by Django 4.2.4 on 2023-09-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles_app', '0005_alter_article_created_time_alter_article_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='تاریخ تولید'),
        ),
    ]
