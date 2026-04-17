from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatMessage

def ai_page(request):
    return render(request, "ai/chat.html")


def ai_chat(request):
    if request.method == "POST":
        message = request.POST.get("message")

        # SIMPLE AI LOGIC (MVP)
        response = generate_response(message)

        ChatMessage.objects.create(
            user_message=message,
            bot_response=response
        )

        return JsonResponse({"response": response})


def generate_response(message):
    message = message.lower()

    if "hello" in message or "bonjour" in message:
        return "Hello 👋 I am Lelo Maurice AI Assistant."
    elif "projects" in message:
        return "You can view my projects on the Projects page 🚀"
    elif "skills" in message:
        return "I specialize in Django, Flutter, DevOps and AI systems ⚡"
    else:
        return "I am still learning 🤖 but I can help you explore the portfolio."