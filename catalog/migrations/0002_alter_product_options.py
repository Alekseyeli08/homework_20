# Generated by Django 5.0.7 on 2024-08-22 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["id"],
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
    ]
