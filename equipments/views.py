# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from equipments.filters import EquipmentFilter
from equipments.forms import EquipmentForm, HistoryRemovalDeliveryEquipmentForm
from equipments.models import Equipment


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


@login_required(login_url="login")
def equipments(request):
    equipments = Equipment.objects.all()
    my_filter = EquipmentFilter(request.GET, queryset=equipments)
    equipments = my_filter.qs
    # Paginação
    paginator = Paginator(equipments, 20)  # show 20 equipments per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "my_filter": my_filter,
    }
    return render(request, "equipments.html", context)


@login_required(login_url="login")
def equipment_view(request, slug):
    equipment = get_object_or_404(Equipment, slug=slug)
    context = {
        "equipment": equipment,
    }
    return render(request, "equipment.html", context)


@login_required(login_url="login")
def equipment_delivery_removal(request, slug):
    if request.method == "POST":
        form = HistoryRemovalDeliveryEquipmentForm(request.POST, request=request)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, "Inserido com sucesso!")
        else:
            messages.add_message(request, constants.ERROR, "Ocorreu um erro!")
        return redirect(
            reverse("equipments:history_equipment_register", kwargs={"slug": slug})
        )
    equipment = get_object_or_404(Equipment, slug=slug)
    form = HistoryRemovalDeliveryEquipmentForm(request=request)
    context = {
        "form": form,
        "equipment": equipment,
    }
    return render(request, "equipment_delivery_removal.html", context)
