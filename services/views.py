from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import render

from services.forms import ServiceForm
from services.models import Service


# Create your views here.
@login_required(login_url="login")
def register_service(request):
    if request.method == "POST":
        form = ServiceForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, "Inserido com sucesso!")
        else:
            messages.add_message(request, constants.ERROR, "Ocorreu um erro!")
    form = ServiceForm(request=request)
    btn = "Cadastrar Atendimento"
    context = {"form": form, "btn": btn}
    return render(request, "register_service.html", context)


@login_required(login_url="login")
def services(request):
    services = Service.objects.all()
    context = {"services": services}
    return render(request, "services.html", context)
