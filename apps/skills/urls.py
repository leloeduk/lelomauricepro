from django.urls import path
from .views import skills_page

urlpatterns = [
    path('', skills_page, name="skills"),
]