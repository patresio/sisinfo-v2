from django.urls import path

from services.views import register_service, services

app_name = "services"

urlpatterns = [
    path("", services, name="services"),
    path("register", register_service, name="register"),
]
