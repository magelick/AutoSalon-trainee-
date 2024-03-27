# Generated by Django 5.0.3 on 2024-03-27 08:57

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [("api", "0001_initial"), ("api", "0002_initial")]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '__first__')
    ]

    operations = [
        migrations.CreateModel(
            name="AutoSalon",
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
                    "name",
                    models.CharField(max_length=128, verbose_name="Name of Autosalon"),
                ),
                (
                    "location",
                    django_countries.fields.CountryField(
                        max_length=128, verbose_name="Location of Autosalon"
                    ),
                ),
                (
                    "balance",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=8,
                        verbose_name="Balance of Autosalon",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Flag is active"),
                ),
                (
                    "customers",
                    models.ManyToManyField(
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Customers of AutoSalon",
                    ),
                ),
            ],
            options={
                "verbose_name": "autosalon",
                "verbose_name_plural": "autosalons",
            },
        ),
        migrations.CreateModel(
            name="Car",
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
                    "model_name",
                    models.CharField(max_length=128, verbose_name="Model of Car"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Flag is active"),
                ),
                (
                    "autosalons",
                    models.ManyToManyField(
                        related_name="cars",
                        to="api.autosalon",
                        verbose_name="Autosalons with Car",
                    ),
                ),
            ],
            options={
                "verbose_name": "car",
                "verbose_name_plural": "cars",
            },
        ),
        migrations.CreateModel(
            name="OptionCar",
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
                ("year", models.DateTimeField(verbose_name="Year of car")),
                ("mileage", models.PositiveIntegerField(verbose_name="Mileage of Car")),
                (
                    "body_type",
                    models.CharField(
                        choices=[
                            ("sedan", "Sedan"),
                            ("coupe", "Coupe"),
                            ("hatchback", "Hatchback"),
                            ("pickup", "Pickup"),
                            ("off-road", "Off-road"),
                            ("sport", "Sport"),
                            ("hyper", "Hyper"),
                            ("suv", "SUV"),
                            ("crossover", "Crossover"),
                            ("minivan", "Minivan"),
                            ("convertible", "Сonvertible"),
                            ("universal", "Universal"),
                        ],
                        max_length=64,
                        verbose_name="Body type of Car",
                    ),
                ),
                (
                    "transmission_type",
                    models.CharField(
                        choices=[("automatic", "Automatic"), ("mechanics", "Mechanic")],
                        max_length=64,
                        verbose_name="Transmission type of Car",
                    ),
                ),
                (
                    "drive_unit_type",
                    models.CharField(
                        choices=[
                            ("complete", "Complete"),
                            ("front", "Front"),
                            ("back", "Back"),
                        ],
                        max_length=64,
                        verbose_name="Drive unit type of Car",
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        choices=[
                            ("red", "Red"),
                            ("blue", "Blue"),
                            ("green", "Green"),
                            ("orange", "Orange"),
                            ("yellow", "Yellow"),
                            ("violet", "Violet"),
                            ("brown", "Brown"),
                            ("black", "Black"),
                            ("grey", "Grey"),
                            ("white", "White"),
                            ("pink", "Pink"),
                        ],
                        max_length=64,
                        verbose_name="Color of Car",
                    ),
                ),
                (
                    "engine_type",
                    models.CharField(
                        choices=[
                            ("petrol", "Petrol"),
                            ("diesel", "Diesel"),
                            ("electro", "Electro"),
                        ],
                        max_length=64,
                        verbose_name="Engine type of Car",
                    ),
                ),
                (
                    "cars",
                    models.ManyToManyField(
                        related_name="options_car",
                        to="api.car",
                        verbose_name="Cars with Option",
                    ),
                ),
            ],
            options={
                "verbose_name": "option of car",
                "verbose_name_plural": "options of car",
            },
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
        migrations.CreateModel(
            name="SpecialOfferOfAutoSalon",
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
                    "name",
                    models.CharField(
                        max_length=64, verbose_name="Name of Special Offer"
                    ),
                ),
                (
                    "descr",
                    models.TextField(verbose_name="Description of Special Offer"),
                ),
                (
                    "discount",
                    models.PositiveIntegerField(
                        verbose_name="Discount of Special Offer"
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Start date of Special Offer"
                    ),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True, verbose_name="End date of Special Offer"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Flag is active"),
                ),
                (
                    "dealer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.autosalon",
                        verbose_name="AutoSalon of that Special Offer",
                    ),
                ),
            ],
            options={
                "verbose_name": "special offer of autosalon",
                "verbose_name_plural": "special offers of autosalons",
            },
        ),
        migrations.CreateModel(
            name="Supplier",
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
                    "name",
                    models.CharField(max_length=128, verbose_name="Name of Supplier"),
                ),
                (
                    "year_of_issue",
                    models.DateTimeField(verbose_name="Year for issue of Supplier"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=8,
                        verbose_name="Price of each cars",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Flag is active"),
                ),
                (
                    "cars",
                    models.ManyToManyField(
                        related_name="suppliers_of_car",
                        to="api.car",
                        verbose_name="Cars, which have Supplier",
                    ),
                ),
            ],
            options={
                "verbose_name": "supplier",
                "verbose_name_plural": "suppliers",
            },
        ),
        migrations.CreateModel(
            name="SpecialOfferOfSupplier",
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
                    "name",
                    models.CharField(
                        max_length=64, verbose_name="Name of Special Offer"
                    ),
                ),
                (
                    "descr",
                    models.TextField(verbose_name="Description of Special Offer"),
                ),
                (
                    "discount",
                    models.PositiveIntegerField(
                        verbose_name="Discount of Special Offer"
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Start date of Special Offer"
                    ),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True, verbose_name="End date of Special Offer"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Flag is active"),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.supplier",
                        verbose_name="Supplier of that Special Offer",
                    ),
                ),
            ],
            options={
                "verbose_name": "special offer of supplier",
                "verbose_name_plural": "special offers of suppliers",
            },
        ),
        migrations.CreateModel(
            name="SaleHistory",
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
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=8,
                        verbose_name="Price of Sale History",
                    ),
                ),
                (
                    "autosalon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sale_history",
                        to="api.autosalon",
                        verbose_name="AutoSalon of Sale History",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sale_history",
                        to="api.supplier",
                        verbose_name="Supplier of Sale History",
                    ),
                ),
            ],
            options={
                "verbose_name": "sale history",
                "verbose_name_plural": "sale histories",
            },
        ),
        migrations.AddField(
            model_name="autosalon",
            name="suppliers",
            field=models.ManyToManyField(
                to="api.supplier", verbose_name="Suppliers of AutoSalon"
            ),
        ),
    ]