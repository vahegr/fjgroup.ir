# Generated by Django 4.2.4 on 2023-09-19 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0004_remove_content_images_content_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='second_cover_image',
            field=models.ImageField(null=True, upload_to='images/content_images', verbose_name='عکس کاور دوم'),
        ),
    ]