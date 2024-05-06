# Generated by Django 5.0.3 on 2024-04-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "services",
            "0004_alter_service_call_alter_service_fullname_employee_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="call",
            field=models.CharField(
                choices=[
                    ("04", "PRESENCIAL"),
                    ("03", "EMAIL"),
                    ("05", "VERBAL"),
                    ("01", "WHATSAPP"),
                    ("99", "OUTROS"),
                    ("02", "TELEFONE"),
                ],
                default="02",
                max_length=2,
                verbose_name="atendimento via",
            ),
        ),
    ]