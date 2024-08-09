import os 
import environ

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .settings.base import BASE_DIR

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

urlpatterns = [
    path(env('ADMIN_URL'), admin.site.urls),
    path('', include('blog.urls')),
    path('user/', include('users.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)