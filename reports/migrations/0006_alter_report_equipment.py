# Generated by Django 5.0.3 on 2024-04-04 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0008_alter_historyremovaldeliveryequipment_room_and_more'),
        ('reports', '0005_report_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='equipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipments.equipment', verbose_name='equipamento'),
        ),
    ]
