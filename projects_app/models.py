from django.db import models
from django.urls import reverse
from unidecode import unidecode
from django.template import defaultfilters


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    persian_title = models.CharField(max_length=200, verbose_name='عنوان فارسی')
    project_type = models.CharField(max_length=100, verbose_name='تایپ پروژه(برای توسعه دهندگان)', default='projectType')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان تولید')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Image(models.Model):
    title = models.CharField(max_length=100, default='title')
    image = models.ImageField(upload_to='images/project_images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'عکس پروژه'
        verbose_name_plural = 'عکس های پروژه ها'


BaseCategory = (
    ('s', 'structure'),
    ('i', 'interior'),
    ('e', 'exterior'),
    ('o', 'object'),
)


class Project(models.Model):
    slug = models.SlugField(allow_unicode=True, blank=True, null=True)
    base_category = models.CharField(max_length=1, choices=BaseCategory, default='s', verbose_name="نوع پروژه")

    cover_image = models.ImageField(upload_to='images/project_images', verbose_name='عکس کاور', default=None)
    images = models.ManyToManyField(Image, verbose_name='عکس های پروژه', default=None)

    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='categories')

    title = models.CharField(max_length=300, verbose_name='عنوان')
    persian_title = models.CharField(max_length=200, verbose_name='عنوان (فارسی)')

    description = models.CharField(max_length=1500, verbose_name='توضیحات')
    persian_description = models.CharField(max_length=1500, verbose_name='توضیحات (فارسی)')

    location = models.CharField(max_length=300, blank=True, verbose_name='مکان')
    persian_location = models.CharField(max_length=300, blank=True, verbose_name='مکان(فارسی)')

    planning = models.CharField(max_length=300, blank=True, verbose_name='برنامه ریزی')
    persian_planning = models.CharField(max_length=300, blank=True, verbose_name='برنامه ریزی(فارسی)')

    engineer = models.CharField(max_length=300, blank=True, verbose_name='مهندس')
    persian_engineer = models.CharField(max_length=300, blank=True, verbose_name='مهندس(فارسی)')

    project_team = models.TextField(max_length=3000, blank=True, verbose_name='تیم پروژه')
    persian_project_team = models.TextField(max_length=3000, blank=True, verbose_name='تیم پروژه(فارسی)')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان تولید')

    def __str__(self):
        return f"{self.title} - {self.description[:30]} ..."

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'

    def get_absolute_url(self):
        return reverse('projects_app:project_detail', args=[self.id, self.slug])

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.title == "":
            self.slug = defaultfilters.slugify(unidecode(self.title))
        super(Project, self).save()


