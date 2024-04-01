# Generated by Django 5.0.3 on 2024-04-01 11:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("api", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="autosalon",
            name="customers",
            field=models.ManyToManyField(
                to=settings.AUTH_USER_MODEL, verbose_name="Customers of AutoSalon"
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="autosalons",
            field=models.ManyToManyField(
                related_name="cars",
                to="api.autosalon",
                verbose_name="Autosalons with Car",
            ),
        ),
        migrations.AddField(
            model_name="optioncar",
            name="cars",
            field=models.ManyToManyField(
                related_name="options_car",
                to="api.car",
                verbose_name="Cars with Option",
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="options",
            field=models.ManyToManyField(
                related_name="cars_options",
                to="api.optioncar",
                verbose_name="Options of Car",
            ),
        ),
        migrations.AddField(
            model_name="salehistory",
            name="autosalon",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sale_history",
                to="api.autosalon",
                verbose_name="AutoSalon of Sale History",
            ),
        ),
        migrations.AddField(
            model_name="specialofferofautosalon",
            name="dealer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="api.autosalon",
                verbose_name="AutoSalon of that Special Offer",
            ),
        ),
        migrations.AddField(
            model_name="supplier",
            name="cars",
            field=models.ManyToManyField(
                related_name="suppliers_of_car",
                to="api.car",
                verbose_name="Cars, which have Supplier",
            ),
        ),
        migrations.AddField(
            model_name="specialofferofsupplier",
            name="supplier",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="api.supplier",
                verbose_name="Supplier of that Special Offer",
            ),
        ),
        migrations.AddField(
            model_name="salehistory",
            name="supplier",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sale_history",
                to="api.supplier",
                verbose_name="Supplier of Sale History",
            ),
        ),
        migrations.AddField(
            model_name="autosalon",
            name="suppliers",
            field=models.ManyToManyField(
                to="api.supplier", verbose_name="Suppliers of AutoSalon"
            ),
        ),
    ]
