from datetime import date, datetime

from django.db import models
from django.shortcuts import resolve_url as r
from django.template.defaultfilters import slugify

from authenticate.models import ProfessionalUser
from dashboard.models import Sector
from equipments.models import Equipment

KIND_SERVICE_CALL = {
    ("01", "WHATSAPP"),
    ("02", "TELEFONE"),
    ("03", "EMAIL"),
    ("04", "PRESENCIAL"),
    ("05", "VERBAL"),
    ("99", "OUTROS"),
}


# Create your models here.
class Service(models.Model):
    number_service = models.CharField(
        "identificação do atendimento",
        max_length=20,
        unique=True,
        blank=True,
        null=True,
    )
    call = models.CharField(
        "atendimento via", max_length=2, choices=KIND_SERVICE_CALL, default="02"
    )
    slug = models.SlugField("slug")
    fullname_employee = models.CharField(
        "nome completo do funcionário(a)", max_length=100, null=True, blank=True
    )
    sector = models.ForeignKey(
        Sector,
        on_delete=models.DO_NOTHING,
        verbose_name="setor",
        related_name="setor",
    )
    room = models.CharField("sala", max_length=20, blank=True)
    professional = models.ForeignKey(
        ProfessionalUser,
        on_delete=models.DO_NOTHING,
        verbose_name="profissional do atendimento",
        related_name="profissional_atendimento",
    )
    pro_accountable = models.ForeignKey(
        ProfessionalUser,
        on_delete=models.DO_NOTHING,
        verbose_name="profissional responsável que monitorará o atendimento",
        related_name="profissional_responsavel_atendimento",
    )
    status = models.BooleanField("status", default=True)
    remote = models.BooleanField("remoto", default=False)
    created_at = models.DateTimeField(
        "criado em",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        "atualizado em",
        auto_now=True,
    )
    details = models.TextField("detalhes do atendimento")

    class Meta:
        ordering = ["-status", "-updated_at", "-created_at"]
        verbose_name = "atendimento"
        verbose_name_plural = "atendimentos"

    def __str__(self):
        return self.number_service

    def get_absolute_url(self):
        return r("services:service-detail", slug=self.slug)

    def days_service_open(self):
        """
        Retorna a quantidade de dias que o atendimento está aberto
        """
        if self.created_at != self.updated_at:
            if self.status:
                return f"{str((date.today() - self.created_at.date()).days)}"
            return ""
        if (date.today() - self.update_at.date()).days > -1:
            return f"{str((date.today() - self.created_at.date()).days)}"

    def days_service_closed(self):
        """
        Retorna quantidade de dias que o atendimento ficou aberto
        """
        if not self.status:
            return f"{str((self.updated_at.date() - self.created_at.date()).days)}"
        return False

    def save(self, *args, **kwargs):
        service = Service.objects.filter(created_at__date=date.today()).count()
        if not self.slug:
            if not self.number_service:
                self.number_service = (
                    datetime.now().strftime("%Y%m%d")
                    + f"{self.sector.id:03}"
                    + f"{(service + 1):03}"
                )
            self.slug = slugify(self.number_service)
        return super().save()


class OrderofService(models.Model):
    KIND_ORDER_OF_SERVICE = {
        ("01", "LIMPEZA"),
        ("02", "REVISÃO DE EQUIPAMENTOS"),
        ("03", "REVISÃO DE SERVIÇOS"),
        ("04", "FORMATAÇÃO"),
        ("05", "AGUARDANDO PEÇAS"),
        ("9A", "AGUARDANDO TERCEIROS"),
        ("9B", "OUTROS"),
    }
    kind_order_of_service = models.CharField(
        "tipo do serviço", max_length=2, choices=KIND_ORDER_OF_SERVICE
    )
    number_order_of_service = models.CharField(
        "número da ordem de serviço", max_length=20, unique=True, blank=True, null=True
    )
    equipment = models.ForeignKey(
        Equipment, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="equipamento na os"
    )
    service = models.ForeignKey(
        Service, on_delete=models.DO_NOTHING, verbose_name="numero do atendimento"
    )
    report = models.ForeignKey(
        "reports.Report", on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="laudo da os"
    )
    professional = models.ForeignKey(
        ProfessionalUser,
        verbose_name="profissional",
        on_delete=models.DO_NOTHING,
    )
    pro_opened = models.ForeignKey(
        ProfessionalUser,
        on_delete=models.DO_NOTHING,
        verbose_name="profissional responsável que monitorará a ordem de serviço",
        related_name="profissional_responsavel_order_of_service",
    )
    status = models.BooleanField("status", default=True)
    remote = models.BooleanField("remoto", default=False)
    problem = models.TextField("descrição do problema")
    solution = models.TextField("descrição da solução")
    created_at = models.DateTimeField("criado em")
    updated_at = models.DateTimeField("atualizado em")
