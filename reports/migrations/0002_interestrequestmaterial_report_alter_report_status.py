# Generated by Django 4.2.7 on 2023-12-04 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("reports", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="interestrequestmaterial",
            name="report",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="reports.report",
                verbose_name="laudo",
            ),
        ),
        migrations.AlterField(
            model_name="report",
            name="status",
            field=models.CharField(
                choices=[("1", "Aberto"), ("2", "Aguardando ..."), ("3", "Finalizado")],
                default=1,
                max_length=1,
                verbose_name="status",
            ),
        ),
    ]