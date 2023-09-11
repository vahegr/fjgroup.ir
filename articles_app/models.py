from datetime import timezone

from django.db import models


# model writen by two type of language
class Article(models.Model):
    image = models.ImageField(upload_to='images/article_images', verbose_name='عکس')
    second_image = models.ImageField(upload_to='images/article_images', null=True, verbose_name='عکس دوم')

    title = models.CharField(max_length=300, verbose_name='عنوان')
    persian_title = models.CharField(max_length=300, verbose_name='عنوان(فارسی)')

    description = models.TextField(max_length=1500, verbose_name='توضیحات')
    persian_description = models.TextField(max_length=1500, verbose_name='توضیحات(فارسی)')

    pdf_file = models.FileField(upload_to='pdfs/article_pdf', verbose_name='فایل')
    created_time = models.DateField(auto_now_add=True, null=True, verbose_name='تاریخ تولید')

    def __str__(self):
        return f'{self.title} - {self.description[:30]}...'

    class Meta:
        ordering = ('-created_time',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
