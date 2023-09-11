from django.shortcuts import render
from .models import Article
from django.http import FileResponse


def articles_view(request):
    articles = Article.objects.all()
    return render(request, 'articles_app/OurArticles.html', context={'articles': articles})


def article_download(request, id):
    article = Article.objects.get(id=id)
    pdf_file = article.pdf_file

    response = FileResponse(pdf_file)
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'

    return response
