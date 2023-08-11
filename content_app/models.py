from django.db import models
from projects_app.models import Image


class Content(models.Model):
    cover_image = models.ImageField(upload_to='images/content_images')
    video = models.FileField(upload_to='videos/content_videos', blank=True)
    images = models.ForeignKey(Image, blank=True, on_delete=models.CASCADE)

    title = models.CharField(max_length=400)
    persian_title = models.CharField(max_length=400)

    description = models.CharField(max_length=1500)
    persian_description = models.CharField(max_length=1500)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان تولید')

    def __str__(self):
        return f'{self.title} - {self.description[:30]}...'

    class Meta:
        ordering = ('-created_at',)


