from django.shortcuts import render
from projects_app.models import Project


def home_view(request):
    recent_projects = Project.objects.all()[:20]
    return render(request, 'home_app/index.html', context={'projects': recent_projects})
