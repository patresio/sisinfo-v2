import django_filters
from django.forms import TextInput
from django_filters import CharFilter

from equipments.models import Equipment


class EquipmentFilter(django_filters.FilterSet):
    patrimony = CharFilter(
        field_name="patrimony",
        lookup_expr="icontains",
        label="Pesquise pelo patrimônio:",
        widget=TextInput(
            attrs={
                "class": "block pt-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 w-full max-w-full",
                "placeholder": "Patrimônio",
            }
        ),
    )
    id_equipment = CharFilter(
        field_name="id_equipment",
        lookup_expr="icontains",
        label="Pesquise pelo id do equipamento:",
        widget=TextInput(
            attrs={
                "class": "block pt-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 w-full max-w-full",
                "placeholder": "Identificação do Equipamento",
            }
        ),
    )

    class Meta:
        model = Equipment
        fields = ["id_equipment", "patrimony", "kind", "sector", "status"]
