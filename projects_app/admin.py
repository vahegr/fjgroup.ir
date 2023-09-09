from django.contrib import admin
from . import models


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('images',)


admin.site.register(models.Category)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Image)
