from django.shortcuts import render
from apps.projects.models import Project

def home(request):
    projects = Project.objects.all().order_by('-created_at')[:3]

    return render(request, "core/home.html", {
        "projects": projects
    })