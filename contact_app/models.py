from django.db import models


class ContactInformation(models.Model):
    phone = models.CharField(max_length=20)
    second_phone = models.CharField(max_length=20)
    third_phone = models.CharField(max_length=20)
    location = models.CharField(max_length=1200)
    email = models.EmailField(max_length=300)

    def __str__(self):
        return f'{self.phone} - {self.email} - {self.location}'

    class Meta:
        verbose_name = 'طلاعات تماس'
        verbose_name_plural = 'اطلاعات تماس'

