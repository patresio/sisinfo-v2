# Generated by Django 5.0.3 on 2024-04-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_alter_service_call'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['status', '-updated_at', '-created_at'], 'verbose_name': 'atendimento', 'verbose_name_plural': 'atendimentos'},
        ),
        migrations.AlterField(
            model_name='service',
            name='call',
            field=models.CharField(choices=[('03', 'EMAIL'), ('04', 'PRESENCIAL'), ('02', 'TELEFONE'), ('05', 'VERBAL'), ('01', 'WHATSAPP'), ('99', 'OUTROS')], default='02', max_length=2, verbose_name='atendimento via'),
        ),
    ]
