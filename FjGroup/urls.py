from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('projects/', include('projects_app.urls')),
    path('about/', include('about_app.urls')),
    path('articles/', include('articles_app.urls')),
    path('content/', include('content_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
