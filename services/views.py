from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from reports.models import Report
from services.filters import ServiceFilter
from services.forms import ServiceForm
from services.models import Service


# Create your views here.
@login_required(login_url="login")
def register_service(request):
    if request.method == "POST":
        form = ServiceForm(request.POST, request=request)
        if form.is_valid():
            slug = form.save()
            messages.add_message(request, constants.SUCCESS, "Inserido com sucesso!")
            return redirect(reverse("services:service-detail", kwargs={"slug": slug}))
        else:
            messages.add_message(request, constants.ERROR, "Ocorreu um erro!")
    form = ServiceForm(request=request)
    btn = "Cadastrar Atendimento"
    context = {"form": form, "btn": btn}
    return render(request, "register_service.html", context)


@login_required(login_url="login")
def services(request):
    services = Service.objects.all()
    my_filter = ServiceFilter(request.GET, queryset=services)
    services = my_filter.qs
    # paginacao
    paginator = Paginator(services, 20)  # show 20 services per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "my_filter": my_filter}
    return render(request, "services.html", context)


@login_required(login_url="login")
def my_services(request):
    services = Service.objects.filter(pro_accountable=request.user)
    my_filter = ServiceFilter(request.GET, queryset=services)
    services = my_filter.qs
    # paginacao
    paginator = Paginator(services, 20)  # show 20 services per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "my_filter": my_filter}
    return render(request, "services.html", context)


@login_required(login_url="login")
def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    reports = Report.objects.filter(service=service.id)
    context = {"service": service, "reports": reports}
    return render(request, "service_detail.html", context)


@login_required(login_url="login")
def service_closed(request, slug):
    service = get_object_or_404(Service, slug=slug)
    service.status = False
    service.save()
    messages.add_message(
        request, constants.SUCCESS, f"Atendimento {service} fechado com sucesso."
    )
    return redirect(reverse("services:services"))


@login_required(login_url="login")
def service_edit(request, slug):
    service = get_object_or_404(Service, slug=slug)
    service.save()
    return redirect(reverse("services:services"))
