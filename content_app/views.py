from django.shortcuts import render
from .models import Content


def content_view(request):
    content = Content.objects.all()
    return render(request, 'content_app/Content.html', context={'content': content})


def content_detail(request, id, slug):
    content = Content.objects.get(id=id, slug=slug)
    return render(request, 'content_app/Content_detail.html', context={'content': content})
