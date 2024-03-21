from django.urls import path

from equipments.views import equipment_register, equipments

app_name = "equipments"


urlpatterns = [
    path("register_equipment", equipment_register, name="register_equipment"),
    path("", equipments, name="equipments"),
]
