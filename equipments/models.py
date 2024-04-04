from datetime import date, datetime

from django.db import models
from django.shortcuts import resolve_url as r
from django.template.defaultfilters import slugify

from authenticate.models import ProfessionalUser
from dashboard.models import Sector


# Create your models here.
class Equipment(models.Model):
    KINDS = (
        ("01", "Computador"),
        ("02", "Tablet"),
        ("03", "Notebook"),
        ("04", "Impressora"),
        ("05", "Celular"),
        ("06", "Monitor"),
        ("07", "Nobreak"),
        ("08", "Estabilizador"),
        ("09", "Relógio de Ponto"),
        ("10", "Switch"),
        ("11", "Outros"),
    )
    id_equipment = models.CharField(
        "identificação do equipamento",
        max_length=30,
        unique=True,
        blank=True,
        null=True,
    )
    slug = models.SlugField("slug")
    patrimony = models.CharField("patrimonio", max_length=10, default="0")
    kind = models.CharField("tipo", max_length=2, choices=KINDS, default="01")
    description = models.TextField("descrição")
    sector = models.ForeignKey(
        Sector,
        on_delete=models.DO_NOTHING,
        verbose_name="setor",
        related_name="setores",
    )
    status = models.BooleanField("status", default=True)
    serial_number = models.CharField(
        "numero de série", default=0, max_length=50, null=True, blank=True
    )

    class Meta:
        ordering = ["id_equipment", "sector", "status", "kind", "patrimony"]
        verbose_name = "equipamento"
        verbose_name_plural = "equipamentos"

    def __str__(self):
        return self.id_equipment

    def get_absolute_url(self):
        return r("equipments:equipment_view", slug=self.slug)

    def save(self, *args, **kwargs):
        count = Equipment.objects.filter(sector=self.sector).count()
        var_id_equipment = (
            "PMNH"
            + f"{self.patrimony:010}"
            + f"{self.sector.id:03}"
            + f"{self.kind:02}"
            + f"{(count + 1):04}"
        )
        if self.patrimony != "0":
            if not self.slug:
                if not self.id_equipment:
                    self.id_equipment = var_id_equipment
                self.slug = slugify(self.id_equipment)
            elif self.id_equipment != var_id_equipment:
                self.id_equipment = var_id_equipment
                self.slug = slugify(self.id_equipment)
        else:
            if not self.slug:
                if not self.id_equipment:
                    self.id_equipment = var_id_equipment
                self.slug = slugify(self.id_equipment)
        return super().save()


class HistoryRemovalDeliveryEquipment(models.Model):
    number_history = models.CharField("historico", max_length=30)
    equipment = models.ForeignKey(
        Equipment, on_delete=models.CASCADE, verbose_name="Equipamento"
    )
    slug = models.SlugField("slug")
    observation = models.TextField("observação")
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, verbose_name="setor")
    room = models.CharField("sala", null=True, blank=True)
    employee = models.CharField("funcionário", max_length=20, null=True)
    professional = models.ForeignKey(
        ProfessionalUser,
        on_delete=models.DO_NOTHING,
        verbose_name="tecnico",
        related_name="tecnico",
    )
    pro_accountable = models.ForeignKey(
        ProfessionalUser,
        on_delete=models.DO_NOTHING,
        verbose_name="tecnico responsavel",
        related_name="responsavel",
    )
    status = models.BooleanField("status", default=False)
    charger = models.BooleanField("carregador", default=False)
    props = models.BooleanField("acessórios", default=False)
    delivery = models.BooleanField("entrega", default=False)
    removal = models.BooleanField("retirada", default=False)
    date = models.DateTimeField("data", auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ["-date", "status"]
        verbose_name = "historico"
        verbose_name_plural = "historicos"

    def __str__(self):
        return self.number_history

    def get_absolute_url(self):
        return r("equipments:history_removal_delivery_view", slug=self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            count = HistoryRemovalDeliveryEquipment.objects.filter(
                date__date=date.today()
            ).count()
            if not self.number_history:
                self.number_history = (
                    datetime.now().strftime("%Y%m%d")
                    + f"{self.equipment.id_equipment[:8]}"
                    + f"{(count + 1):03}"
                )
            self.slug = slugify(self.number_history)
        return super().save()
