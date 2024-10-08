# Generated by Django 5.0.7 on 2024-09-07 23:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_product_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
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
                (
                    "version_number",
                    models.IntegerField(default=0, verbose_name="номер версии"),
                ),
                ("version_name", models.TextField(verbose_name="название версии")),
                (
                    "version_indicator",
                    models.BooleanField(default=True, verbose_name="актуалная версия"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="versions",
                        to="catalog.product",
                        verbose_name="продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Верссия",
                "verbose_name_plural": "Версии",
            },
        ),
    ]
