from django.shortcuts import render
from apps.projects.models import Project
from apps.skills.models import Skill

def home(request):
    projects = Project.objects.all().order_by('-created_at')[:3]
    skills = Skill.objects.all()[:6]

    return render(request, "core/home.html", {
        "projects": projects,
        "skills": skills
    })