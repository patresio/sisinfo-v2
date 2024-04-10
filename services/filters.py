import django_filters
from django.forms import DateInput, TextInput
from django_filters import CharFilter, DateFilter

from services.models import Service


class ServiceFilter(django_filters.FilterSet):
    start_date = DateFilter(
        field_name="created_at",
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
        field_name="created_at",
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
    details = CharFilter(
        field_name="details",
        lookup_expr="icontains",
        label="Pesquise por detalhes do atendimento:",
        widget=TextInput(
            attrs={
                "class": "block pt-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 w-full max-w-full",
                "placeholder": "Detalhes",
            }
        ),
    )
    number_service = CharFilter(
        field_name="number_service",
        lookup_expr="icontains",
        label="Pesquise pelo protocolo do atendimento:",
        widget=TextInput(
            attrs={
                "class": "block pt-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 w-full max-w-full",
                "placeholder": "Protocolo do atendimento",
            }
        ),
    )
    room = CharFilter(
        field_name="room",
        lookup_expr="icontains",
        label="Pesquise pela sala:",
        widget=TextInput(
            attrs={
                "class": "block pt-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 w-full max-w-full",
                "placeholder": "Sala",
            }
        ),
    )

    fullname_employee = CharFilter(
        field_name="fullname_employee",
        lookup_expr="icontains",
        label="Pesquise pelo(a) funcionário(a):",
        widget=TextInput(
            attrs={
                "class": "block pt-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 w-full max-w-full",
                "placeholder": "Funcionário(a)",
            }
        ),
    )

    class Meta:
        model = Service
        fields = "__all__"
        exclude = ["created_at", "slug", "updated_at"]
