from rest_framework.serializers import ModelSerializer, IntegerField, DecimalField
from .models import (
    AutoSalon,
    Car,
    OptionCar,
    Supplier,
    SaleHistory,
    SpecialOfferOfAutoSalon,
    SpecialOfferOfSupplier,
)

from .utils import AutoSalonStatsService, SupplierStatsService


class AutoSalonSerializer(ModelSerializer):
    """
    Serializer for AutoSalon model
    """

    class Meta:
        model = AutoSalon
        fields = "__all__"


class CarSerializer(ModelSerializer):
    """
    Serializer for Car model
    """

    class Meta:
        model = Car
        fields = "__all__"


class OptionCarSerializer(ModelSerializer):
    """
    Serializer for OptionCar model
    """

    class Meta:
        model = OptionCar
        fields = "__all__"


class SupplierSerializer(ModelSerializer):
    """
    Serializer for Supplier model
    """

    class Meta:
        model = Supplier
        fields = "__all__"


class SaleHistorySerializer(ModelSerializer):
    """
    Serializer for SaleHistory model
    """

    class Meta:
        model = SaleHistory
        fields = "__all__"


class SpecialOfferOfAutoSalonSerializer(ModelSerializer):
    """
    Serializer for SpecialOfferOfAutoSalon model
    """

    class Meta:
        model = SpecialOfferOfAutoSalon
        fields = "__all__"


class SpecialOfferOfSupplierSerializer(ModelSerializer):
    """
    Serializer for SpecialOfferOfSupplier model
    """

    class Meta:
        model = SpecialOfferOfSupplier
        fields = "__all__"


class AutoSalonStatsSerializer(ModelSerializer):
    """
    Serializer for AutosSalonStatsViewSet
    """

    suppliers_count = IntegerField(read_only=True)
    cars_count = IntegerField(read_only=True)
    total_price = DecimalField(max_digits=10, decimal_places=2, read_only=True)
    special_customers = IntegerField(read_only=True)
    car_price = DecimalField(max_digits=10, decimal_places=2, read_only=True)
    sale_history_count = IntegerField(read_only=True)
    prices_in_sale_histories = DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = AutoSalon
        fields = (
            "suppliers_count",
            "cars_count",
            "total_price",
            "special_customers",
            "car_price",
            "sale_history_count",
            "prices_in_sale_histories",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["suppliers_count"] = AutoSalonStatsService.get_suppliers_count()
        data["cars_count"] = AutoSalonStatsService.get_cars_count()
        data["total_price"] = AutoSalonStatsService.get_total_price()
        data["special_customers"] = AutoSalonStatsService.get_special_customers()
        data["car_price"] = AutoSalonStatsService.get_car_price()
        data["sale_history_count"] = AutoSalonStatsService.get_sale_history_count()
        data["prices_in_sale_histories"] = (
            AutoSalonStatsService.get_prices_in_sale_histories()
        )

        return data


class SupplierStatsSerializer(ModelSerializer):
    """
    Serializer for SupplierStatsViewSet
    """

    total_prices = DecimalField(max_digits=10, decimal_places=2, read_only=True)
    autosalons_count = IntegerField(read_only=True)
    cars_count = IntegerField(read_only=True)
    sale_history_count = IntegerField(read_only=True)
    prices_in_sale_histories = DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = Supplier
        fields = (
            "total_prices",
            "autosalons_count",
            "cars_count",
            "sale_history_count",
            "prices_in_sale_histories",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["total_prices"] = SupplierStatsService.get_total_prices()
        data["autosalons_count"] = SupplierStatsService.get_autosalons_count()
        data["cars_count"] = SupplierStatsService.get_cars_count()
        data["sale_history_count"] = SupplierStatsService.get_sale_history_count()
        data["prices_in_sale_histories"] = (
            SupplierStatsService.get_prices_in_sale_histories()
        )

        return data
