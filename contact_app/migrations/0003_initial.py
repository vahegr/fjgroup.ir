# Generated by Django 4.2.4 on 2023-09-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact_app', '0002_delete_contactinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_title', models.CharField(max_length=100, verbose_name='شهر یا کشور')),
                ('persian_location_title', models.CharField(max_length=100, verbose_name='شهر یا کشور(فارسی)')),
                ('location', models.CharField(max_length=1200, verbose_name='آدرس')),
                ('persian_location', models.CharField(max_length=1200, verbose_name='آدرس(فارسی)')),
                ('contact', models.CharField(max_length=200, verbose_name='تماس')),
                ('persian_contact', models.CharField(max_length=200, verbose_name='تماس(فارسی)')),
                ('phone', models.CharField(max_length=20, verbose_name='شماره تلفن')),
                ('second_phone', models.CharField(blank=True, max_length=20, verbose_name='شماره تلفن دوم')),
                ('email', models.EmailField(max_length=300, verbose_name='آدرس ایمیل')),
            ],
            options={
                'verbose_name': 'طلاعات تماس',
                'verbose_name_plural': 'اطلاعات تماس',
            },
        ),
    ]