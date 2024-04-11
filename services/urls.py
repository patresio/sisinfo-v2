from django.urls import path

from services.views import (
    my_services,
    register_service,
    service_closed,
    service_detail,
    service_edit,
    services,
)

app_name = "services"

urlpatterns = [
    path("", services, name="services"),
    path("my-services", my_services, name="my-services"),
    path("register", register_service, name="register"),
    path("<slug:slug>", service_detail, name="service-detail"),
    path("closed/<slug:slug>", service_closed, name="service-closed"),
    path("update/<slug:slug>", service_edit, name="service-edit"),
]
