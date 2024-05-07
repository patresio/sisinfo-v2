# Generated by Django 5.0.3 on 2024-05-07 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_alter_service_call'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='call',
            field=models.CharField(choices=[('04', 'PRESENCIAL'), ('02', 'TELEFONE'), ('99', 'OUTROS'), ('05', 'VERBAL'), ('03', 'EMAIL'), ('01', 'WHATSAPP')], default='02', max_length=2, verbose_name='atendimento via'),
        ),
    ]
