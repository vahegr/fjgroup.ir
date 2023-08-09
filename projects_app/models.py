from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    persian_title = models.CharField(max_length=200, verbose_name='عنوان فارسی')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان تولید')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Project(models.Model):
    category = models.ManyToManyField(Category, verbose_name='دسته بندی')
    title = models.CharField(max_length=300, verbose_name='عنوان')
    persian_title = models.CharField(max_length=200, verbose_name='عنوان فارسی')
    description = models.CharField(max_length=1500, verbose_name='توضیحات')
    persian_description = models.CharField(max_length=1500, verbose_name='توضیحات فارسی')

    location = models.CharField(max_length=300, blank=True)
    persian_location = models.CharField(max_length=300, blank=True)

    builder = models.CharField(max_length=300, blank=True)
    persian_builder = models.CharField(max_length=300, blank=True)

    project_management = models.CharField(max_length=300, blank=True)
    persian_project_management = models.CharField(max_length=300, blank=True)

    competition = models.CharField(max_length=300, blank=True)
    persian_competition = models.CharField(max_length=300, blank=True)

    ranking = models.CharField(max_length=300, blank=True)
    persian_ranking = models.CharField(max_length=300, blank=True)

    planing = models.CharField(max_length=300, blank=True)
    persian_planing = models.CharField(max_length=300, blank=True)

    start_of_construction = models.CharField(max_length=300, blank=True)
    persian_start_of_construction = models.CharField(max_length=300, blank=True)

    completion = models.CharField(max_length=300, blank=True)
    persian_completion = models.CharField(max_length=300, blank=True)

    gross_floor_area = models.CharField(max_length=300, blank=True)
    persian_gross_floor_area = models.CharField(max_length=300, blank=True)

    images_copyright = models.CharField(max_length=300, blank=True)
    persian_images_copyright = models.CharField(max_length=300, blank=True)

    project_team = models.TextField(max_length=3000, blank=True)
    persian_project_team = models.TextField(max_length=3000, blank=True)

    def __str__(self):
        return f"{self.title} - {self.description[:30]} ..."

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'

