from django.db import models


class TeamMember(models.Model):
    image = models.ImageField(upload_to='images/team_members_images', verbose_name='عکس')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    persian_full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی(فارسی)')
    job = models.CharField(max_length=120, verbose_name='شغل')
    persian_job = models.CharField(max_length=120, verbose_name='شغل(فارسی)')
    bio = models.CharField(max_length=500, verbose_name='بایو')
    persian_bio = models.CharField(max_length=500, verbose_name='بایو(فارسی)')
    pdf_file = models.FileField(upload_to='pdfs/article_pdf', verbose_name='فایل')

    def __str__(self):
        return f'{self.full_name} - {self.bio[:30]}...'

    class Meta:
        verbose_name = 'عضو تیم'
        verbose_name_plural = 'افراد تیم'
