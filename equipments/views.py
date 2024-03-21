# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import redirect, render
from django.urls import reverse

from equipments.forms import EquipmentForm


# Create your views here.
@login_required(login_url="login")
def equipment_register(request):
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, "Inserido com sucesso!")
        else:
            messages.add_message(request, constants.ERROR, "Ocorreu um erro!")
        return redirect(reverse("equipments:register_equipment"))
    form = EquipmentForm()
    context = {"form": form, "btn": "Cadastrar Novo Equipamento"}
    return render(request, "equipment_register.html", context)
