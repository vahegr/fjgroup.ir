from django.shortcuts import render
from .models import Project, Category, Image


def structure_projects_view(request):
    structure_projects = Project.objects.filter(base_category='s')
    categories = Category.objects.all()
    return render(request, 'projects_app/projects.html', context={'projects': structure_projects, 'categories': categories})


def interior_projects_view(request):
    interior_projects = Project.objects.filter(base_category='i')
    categories = Category.objects.all()
    return render(request, 'projects_app/projects.html', context={'projects': interior_projects, 'categories': categories})


def exterior_projects_view(request):
    exterior_projects = Project.objects.filter(base_category='e')
    categories = Category.objects.all()
    return render(request, 'projects_app/projects.html', context={'projects': exterior_projects, 'categories': categories})


def objects_projects_view(request):
    objects_projects = Project.objects.filter(base_category='o')
    categories = Category.objects.all()
    return render(request, 'projects_app/projects.html', context={'projects': objects_projects, 'categories': categories})


def project_detail(request, id, slug):
    project = Project.objects.get(id=id, slug=slug)
    return render(request, 'projects_app/Project_detail.html', context={'project': project})
