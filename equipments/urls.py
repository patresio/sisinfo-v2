from django.urls import path

from equipments.views import equipment_register

app_name = "equipments"


urlpatterns = [
    path("register_equipment", equipment_register, name="register_equipment"),
]
