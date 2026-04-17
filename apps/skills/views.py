from django.shortcuts import render
from .models import Skill

def skills_page(request):
    skills = Skill.objects.all()
    return render(request, "skills/skills.html", {"skills": skills})