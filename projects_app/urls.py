from django.urls import path
from . import views

app_name = 'projects_app'

urlpatterns = [
    path('structure', views.structure_projects_view, name='structure'),
    path('interior', views.interior_projects_view, name='interior'),
    path('exterior', views.exterior_projects_view, name='exterior'),
    path('objects', views.objects_projects_view, name='objects'),
    path('project_detail/<int:id>/<slug:slug>', views.project_detail, name='project_detail'),
    path('search', views.search_result, name='search_result'),
]
