# Generated by Django 5.0.3 on 2024-04-05 13:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_service_call_alter_service_room'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='call',
            field=models.CharField(choices=[('01', 'WHATSAPP'), ('99', 'OUTROS'), ('02', 'TELEFONE'), ('04', 'PRESENCIAL'), ('05', 'VERBAL'), ('03', 'EMAIL')], default='02', max_length=2, verbose_name='atendimento via'),
        ),
        migrations.AlterField(
            model_name='service',
            name='fullname_employee',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='nome completo do funcionário(a)'),
        ),
        migrations.AlterField(
            model_name='service',
            name='pro_accountable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profissional_responsavel_atendimento', to=settings.AUTH_USER_MODEL, verbose_name='profissional responsável que monitorará o atendimento'),
        ),
        migrations.AlterField(
            model_name='service',
            name='professional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profissional_atendimento', to=settings.AUTH_USER_MODEL, verbose_name='profissional do atendimento'),
        ),
    ]
