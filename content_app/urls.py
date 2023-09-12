from django.urls import path
from . import views

app_name = 'content_app'

urlpatterns = [
    path('', views.content_view, name='content'),
    path('content_detail/<int:id>/<slug:slug>', views.content_detail, name='content_detail'),
]
