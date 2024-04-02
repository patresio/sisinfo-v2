from django.urls import path

from equipments.views import (
    equipment_delivery_removal,
    equipment_register,
    equipment_update,
    equipment_view,
    equipments,
    history_removal_delivery_view,
)

app_name = "equipments"


urlpatterns = [
    path("", equipments, name="equipments"),
    path("register_equipment", equipment_register, name="register_equipment"),
    path("<slug:slug>/update_equipment", equipment_update, name="update_equipment"),
    path("<slug:slug>", equipment_view, name="equipment_view"),
    path(
        "history/<slug:slug>/register",
        equipment_delivery_removal,
        name="history_equipment_register",
    ),
    path(
        "history/<slug:slug>/view",
        history_removal_delivery_view,
        name="history_removal_delivery_view",
    ),
]
