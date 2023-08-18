# Generated by Django 4.2.4 on 2023-08-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('second_phone', models.CharField(max_length=20)),
                ('third_phone', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=1200)),
                ('email', models.EmailField(max_length=300)),
            ],
            options={
                'verbose_name': 'طلاعات تماس',
                'verbose_name_plural': 'اطلاعات تماس',
            },
        ),
    ]
