# Generated by Django 5.0.3 on 2024-05-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_alter_service_call_delete_orderofservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='call',
            field=models.CharField(choices=[('05', 'VERBAL'), ('03', 'EMAIL'), ('04', 'PRESENCIAL'), ('01', 'WHATSAPP'), ('02', 'TELEFONE'), ('99', 'OUTROS')], default='02', max_length=2, verbose_name='atendimento via'),
        ),
    ]