import django_filters
from django.forms import DateInput, TextInput
from django_filters import CharFilter, DateFilter

from equipments.models import Equipment, HistoryRemovalDeliveryEquipment


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


class HistoryRemovalDeliveryEquipmentFilter(django_filters.FilterSet):
    number_history = CharFilter(
        field_name="number_history",
        lookup_expr="icontains",
        label="Pesquise pelo número do histórico:",
        widget=TextInput(
            attrs={
                "class": "block pt-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 w-full max-w-full",
                "placeholder": "Número do histórico",
            }
        ),
    )
    start_date = DateFilter(
        field_name="date",
        lookup_expr="gte",
        widget=DateInput(
            format=("%Y/%m/%d"),
            attrs={
                "type": "text",
                "datepicker": "",
                "datepicker-buttons": "",
                "datepicker-format": "yyyy-mm-dd",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "A partir de:",
            },
        ),
    )
    end_date = DateFilter(
        field_name="date",
        lookup_expr="lte",
        widget=DateInput(
            format=("%Y/%m/%d"),
            attrs={
                "type": "text",
                "datepicker": "",
                "datepicker-buttons": "",
                "datepicker-format": "yyyy-mm-dd",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "Até",
            },
        ),
    )

    class Meta:
        model = HistoryRemovalDeliveryEquipment
        fields = "__all__"
        exclude = ["date", "slug", "observation", "equipment"]
