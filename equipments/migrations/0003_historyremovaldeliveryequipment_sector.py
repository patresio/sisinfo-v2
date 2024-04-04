# Generated by Django 5.0.3 on 2024-03-22 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_material_supplier_alter_material_bidding'),
        ('equipments', '0002_alter_historyremovaldeliveryequipment_equipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyremovaldeliveryequipment',
            name='sector',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.sector', verbose_name='Setor'),
            preserve_default=False,
        ),
    ]