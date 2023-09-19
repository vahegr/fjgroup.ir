from django.db import models
from projects_app.models import Image
from django.urls import reverse
from unidecode import unidecode
from django.template import defaultfilters


class Content(models.Model):
    slug = models.SlugField(allow_unicode=True, blank=True, null=True)
    cover_image = models.ImageField(upload_to='images/content_images', verbose_name='عکس کاور')
    second_cover_image = models.ImageField(upload_to='images/content_images', verbose_name='عکس کاور دوم', null=True)
    video = models.FileField(upload_to='videos/content_videos', blank=True, verbose_name='ویدیو')
    image = models.ImageField(upload_to='images/content_images', blank=True, verbose_name='عکس')

    title = models.CharField(max_length=400, verbose_name='عنوان')
    persian_title = models.CharField(max_length=400, verbose_name='عنوان(فارسی)')

    description = models.CharField(max_length=1500, verbose_name='توضیحات')
    persian_description = models.CharField(max_length=1500, verbose_name='توضیحات(فارسی)')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان تولید')

    def __str__(self):
        return f'{self.title} - {self.description[:30]}...'

    class Meta:
        verbose_name = 'محتوا'
        verbose_name_plural = 'محتوا'
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse('content_app:content_detail', args=[self.id, self.slug])

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.title == "":
            self.slug = defaultfilters.slugify(unidecode(self.title))
        super(Content, self).save()


