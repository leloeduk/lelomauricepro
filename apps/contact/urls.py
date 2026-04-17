from django.urls import path
from .views import contact_success, contact_view

urlpatterns = [
    path('', contact_view, name="contact"),
    path('success/', contact_success, name="success"),
]