# Generated by Django 4.2.4 on 2023-08-11 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/article_images')),
                ('title', models.CharField(max_length=300)),
                ('persian_title', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=1500)),
                ('persian_description', models.TextField(max_length=1500)),
                ('pdf_file', models.FileField(upload_to='pdfs/article_pdf')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]
