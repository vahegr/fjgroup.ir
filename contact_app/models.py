from django.db import models


class ContactInformation(models.Model):
    location_title = models.CharField(max_length=100, verbose_name='شهر یا کشور')
    persian_location_title = models.CharField(max_length=100, verbose_name='شهر یا کشور(فارسی)')
    location = models.CharField(max_length=1200, verbose_name='آدرس')
    persian_location = models.CharField(max_length=1200, verbose_name='آدرس(فارسی)')
    contact = models.CharField(max_length=200, verbose_name='تماس')
    persian_contact = models.CharField(max_length=200, verbose_name='تماس(فارسی)')
    phone = models.CharField(max_length=20, verbose_name='شماره تلفن')
    second_phone = models.CharField(max_length=20, blank=True, verbose_name='شماره تلفن دوم')
    email = models.EmailField(max_length=300, verbose_name='آدرس ایمیل')

    def __str__(self):
        return f'{self.location_title} - {self.contact} - {self.phone}'

    class Meta:
        verbose_name = 'طلاعات تماس'
        verbose_name_plural = 'اطلاعات تماس'

