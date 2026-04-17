from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import ContactMessage

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # SAVE CRM
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # SEND EMAIL
        send_mail(
            subject=f"[Portfolio] {subject}",
            message=f"""
Name: {name}
Email: {email}

Message:
{message}
""",
            from_email=email,
            recipient_list=["leloeduk2025@gmail.com"],
            fail_silently=False,
        )

        return redirect("/contact/success/")

    return render(request, "contact/contact.html")