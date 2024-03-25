from django.contrib import admin
from .models import (
    AutoSalon,
    Car,
    OptionCar,
    Supplier,
    SaleHistory,
    SpecialOfferOfSupplier,
    SpecialOfferOfAutoSalon,
)


@admin.register(AutoSalon)
class AutoSalonAdmin(admin.ModelAdmin):
    """
    Register AutoSalon's model in admin
    """

    search_fields = ("name",)
    list_display = ("name", "location")
    ordering = ("name", "location", "balance")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """
    Register Car's model in admin
    """

    search_fields = ("model_name",)
    list_display = ("model_name",)
    ordering = ("model_name",)


@admin.register(OptionCar)
class OptionCarAdmin(admin.ModelAdmin):
    """
    Register OptionCar's model in admin
    """

    search_fields = ("year", "mileage")
    list_display = (
        "body_type",
        "transmission_type",
        "drive_unit_type",
        "color",
        "engine_type",
    )
    ordering = ("year", "mileage")


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """
    Register Supplier's model in admin
    """

    search_fields = ("name", "year_of_issue")
    list_display = ("name",)
    ordering = ("name", "year_of_issue")


@admin.register(SaleHistory)
class SaleHistoryAdmin(admin.ModelAdmin):
    """
    Register SaleHistory's model in admin
    """

    search_fields = ("autosalon", "supplier")
    ordering = ("autosalon", "supplier", "price")


@admin.register(SpecialOfferOfAutoSalon)
class SpecialOfferOfAutoSalonAdmin(admin.ModelAdmin):
    """
    Register SpecialOfferOfAutoSalon's model in admin
    """

    search_fields = ("name", "dealer", "discount")
    list_display = ("name", "descr")
    ordering = ("name", "dealer", "discount")


@admin.register(SpecialOfferOfSupplier)
class SpecialOfferOfSupplierAdmin(admin.ModelAdmin):
    """
    Register SpecialOfferOfSupplier's model in admin
    """

    search_fields = ("name", "supplier", "discount")
    list_display = ("name", "descr")
    ordering = ("name", "supplier", "discount")
