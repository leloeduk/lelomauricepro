from django.shortcuts import render
from .models import VisitorLog

def dashboard(request):
    logs = VisitorLog.objects.all().order_by('-created_at')[:50]

    return render(request, "analytics/dashboard.html", {
        "logs": logs
    })