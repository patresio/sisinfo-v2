from django.urls import path

from equipments.views import (
    equipment_delivery_removal,
    equipment_register,
    equipment_view,
    equipments,
)

app_name = "equipments"


urlpatterns = [
    path("", equipments, name="equipments"),
    path("<slug:slug>", equipment_view, name="equipment_view"),
    path(
        "history/<slug:slug>",
        equipment_delivery_removal,
        name="history_equipments",
    ),
    # path("equipments/history/<slug:slug>", equipment_view, name="equipment_view"),
    path("register_equipment", equipment_register, name="register_equipment"),
]
