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
    persian_title = models.CharField(max_length=200, verbose_name='عنوان (فارسی)')
    description = models.CharField(max_length=1500, verbose_name='توضیحات')
    persian_description = models.CharField(max_length=1500, verbose_name='توضیحات (فارسی)')

    location = models.CharField(max_length=300, blank=True, verbose_name='مکان')
    persian_location = models.CharField(max_length=300, blank=True, verbose_name='مکان(فارسی)')

    builder = models.CharField(max_length=300, blank=True, verbose_name='سازنده')
    persian_builder = models.CharField(max_length=300, blank=True, verbose_name='سازنده(فارسی)')

    project_management = models.CharField(max_length=300, blank=True, verbose_name='مدیریت پروژه')
    persian_project_management = models.CharField(max_length=300, blank=True, verbose_name='مدیریت پروژه(فارسی)')

    competition = models.CharField(max_length=300, blank=True, verbose_name='رقابت')
    persian_competition = models.CharField(max_length=300, blank=True, verbose_name='رقابت(فارسی)')

    ranking = models.CharField(max_length=300, blank=True, verbose_name='رتبه بندی')
    persian_ranking = models.CharField(max_length=300, blank=True, verbose_name='رتبه بندی(فارسی)')

    planing = models.CharField(max_length=300, blank=True, verbose_name='تاریخ برنامه ریزی')
    persian_planing = models.CharField(max_length=300, blank=True, verbose_name='تاریخ برنامه ریزی(فارسی)')

    start_of_construction = models.CharField(max_length=300, blank=True, verbose_name='شروع ساخت و ساز')
    persian_start_of_construction = models.CharField(max_length=300, blank=True, verbose_name='شروع ساخت و ساز(فارسی)')

    completion = models.CharField(max_length=300, blank=True, verbose_name='تاریخ تکمیل')
    persian_completion = models.CharField(max_length=300, blank=True, verbose_name='تاریخ تکمیل(فارسی)')

    gross_floor_area = models.CharField(max_length=300, blank=True, verbose_name='مساحت طبقه ناخالص')
    persian_gross_floor_area = models.CharField(max_length=300, blank=True, verbose_name='مساحت طبقه ناخالص(فارسی)')

    # images_copyright = models.CharField(max_length=300, blank=True, verbose_name='')
    # persian_images_copyright = models.CharField(max_length=300, blank=True, verbose_name='')

    project_team = models.TextField(max_length=3000, blank=True, verbose_name='تیم پروژه')
    persian_project_team = models.TextField(max_length=3000, blank=True, verbose_name='تیم پروژه(فارسی)')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان تولید')

    def __str__(self):
        return f"{self.title} - {self.description[:30]} ..."

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'

