from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('projects/', include('apps.projects.urls')),
    path('skills/', include('apps.skills.urls')),
    path('contact/', include('apps.contact.urls')),
    path('ai/', include('apps.ai.urls')),
    path('analytics/', include('apps.analytics.urls')),

]