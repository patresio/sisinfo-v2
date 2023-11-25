# Generated by Django 4.2.7 on 2023-11-25 00:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authenticate", "0003_alter_professionaluser_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="professionaluser",
            name="profile_pic",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/profiles_pic/",
                verbose_name="foto perfil",
            ),
        ),
    ]
