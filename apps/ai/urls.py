from django.urls import path
from .views import ai_page, ai_chat

urlpatterns = [
    path('', ai_page, name="ai"),
    path('chat/', ai_chat, name="ai_chat"),
]