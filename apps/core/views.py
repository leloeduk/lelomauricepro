from django.shortcuts import render
from .models import SiteHeader
from apps.skills.models import Skill
from apps.projects.models import Project

def home(request):
    header = SiteHeader.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()

    return render(request, 'core/home.html', {
        'header': header,
        'skills': skills,
        'projects': projects
    })