# Generated by Django 4.1.2 on 2022-10-12 21:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sistema",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descricao", models.TextField(max_length=10000)),
                (
                    "data_cadastro",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
    ]
