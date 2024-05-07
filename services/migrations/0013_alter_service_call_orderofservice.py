# Generated by Django 5.0.3 on 2024-05-07 12:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0010_alter_equipment_serial_number'),
        ('services', '0012_alter_service_call'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='call',
            field=models.CharField(choices=[('03', 'EMAIL'), ('01', 'WHATSAPP'), ('99', 'OUTROS'), ('02', 'TELEFONE'), ('04', 'PRESENCIAL'), ('05', 'VERBAL')], default='02', max_length=2, verbose_name='atendimento via'),
        ),
        migrations.CreateModel(
            name='OrderofService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_order_of_service', models.CharField(choices=[('05', 'AGUARDANDO PEÇAS'), ('02', 'REVISÃO DE EQUIPAMENTOS'), ('9A', 'AGUARDANDO TERCEIROS'), ('04', 'FORMATAÇÃO'), ('9B', 'OUTROS'), ('03', 'REVISÃO DE SERVIÇOS'), ('01', 'LIMPEZA')], max_length=2, verbose_name='tipo do serviço')),
                ('number_order_of_service', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='número da ordem de serviço')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('remote', models.BooleanField(default=False, verbose_name='remoto')),
                ('problem', models.TextField(verbose_name='descrição do problema')),
                ('solution', models.TextField(verbose_name='descrição da solução')),
                ('created_at', models.DateTimeField(verbose_name='criado em')),
                ('updated_at', models.DateTimeField(verbose_name='atualizado em')),
                ('equipment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='equipments.equipment')),
                ('pro_opened', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profissional_responsavel_order_of_service', to=settings.AUTH_USER_MODEL, verbose_name='profissional responsável que monitorará a ordem de serviço')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='profissional')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='services.service', verbose_name='numero do atendimento')),
            ],
        ),
    ]
