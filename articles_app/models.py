from datetime import timezone

from django.db import models


# model writen by two type of language
class Article(models.Model):
    image = models.ImageField(upload_to='images/article_images')

    title = models.CharField(max_length=300)
    persian_title = models.CharField(max_length=300)

    description = models.TextField(max_length=1500)
    persian_description = models.TextField(max_length=1500)

    pdf_file = models.FileField(upload_to='pdfs/article_pdf')
    created_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.description[:30]}...'

    class Meta:
        ordering = ('-created_time',)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
