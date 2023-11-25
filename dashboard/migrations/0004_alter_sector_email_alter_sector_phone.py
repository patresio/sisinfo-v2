# Generated by Django 4.2.7 on 2023-11-09 13:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0003_alter_sector_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sector",
            name="email",
            field=models.EmailField(max_length=254, null=True, verbose_name="email"),
        ),
        migrations.AlterField(
            model_name="sector",
            name="phone",
            field=models.CharField(max_length=11, null=True, verbose_name="telefone"),
        ),
    ]
