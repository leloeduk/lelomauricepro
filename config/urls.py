from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('projects/', include('apps.projects.urls')),
    path('skills/', include('apps.skills.urls')),
    path('contact/', include('apps.contact.urls')),
    path('ai/', include('apps.ai.urls')),
    path('analytics/', include('apps.analytics.urls')),
]

# MEDIA + STATIC (DEV ONLY)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)