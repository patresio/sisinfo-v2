from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import render

from services.forms import ServiceForm


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
    context = {}
    return render(request, "register_service.html", context)
