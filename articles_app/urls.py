from django.urls import path
from . import views

app_name = 'article_app'

urlpatterns = [
    path('', views.articles_view, name='articles'),
    path('article_download/<int:id>', views.article_download, name='article_download'),
]
