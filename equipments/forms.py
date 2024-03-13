from django import forms

from equipments.models import Equipment, HistoryRemovalDeliveryEquipment


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ["patrimony", "kind", "description", "sector", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field not in [self.fields["description"]]:
                field.widget.attrs["class"] = (
                    "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                )
            else:
                field.widget.attrs["class"] = (
                    "block p-2.5 px-0 mt-1 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                )
                field.widget.attrs["rows"] = "4"


class HistoryRemovalDelivreyEquipmentForm(forms.ModelForm):

    class Meta:
        model = HistoryRemovalDeliveryEquipment
        fields = [
            "equipment",
            "observation",
            "employee",
            "professional",
            "pro_accountable",
            "status",
            "charger",
            "props",
            "delivery",
            "removal",
        ]

    def clean_employee(self):
        employee = self.cleaned_data["employee"]
        words = [w.capitalize() for w in employee.split()]
        return " ".join(words)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")  # store value of request
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field in [self.fields["observation"]]:
                field.widget.attrs["class"] = (
                    "block p-2.5 px-0 mt-1 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                )
                field.widget.attrs["rows"] = "4"
            elif field not in [
                self.fields["status"],
                self.fields["charger"],
                self.fields["props"],
                self.fields["delivery"],
                self.fields["removal"],
            ]:
                field.widget.attrs["class"] = (
                    "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                )
            else:
                field.widget.attrs["class"] = "sr-only peer"
