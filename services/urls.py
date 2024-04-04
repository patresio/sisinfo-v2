from django.urls import path

from services.views import register_service

app_name = "services"

urlpatterns = [path("register", register_service, name="register")]
