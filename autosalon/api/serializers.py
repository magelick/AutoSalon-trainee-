from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
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

    def to_representation(self, instance):
        """
        Representation CountryField instance in str
        :param instance:
        :return:
        """
        representation = super().to_representation(instance)
        representation["location"] = str(instance.location)
        return representation

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

    suppliers_count = SerializerMethodField()
    cars_count = SerializerMethodField()
    total_price = SerializerMethodField()
    special_customers = SerializerMethodField()
    car_price = SerializerMethodField()
    sale_history_count = SerializerMethodField()
    prices_in_sale_histories = SerializerMethodField()

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

    def get_suppliers_count(self, obj):
        return AutoSalonStatsService.get_suppliers_count()

    def get_cars_count(self, obj):
        return AutoSalonStatsService.get_cars_count()

    def get_total_price(self, obj):
        return AutoSalonStatsService.get_total_price()

    def get_special_customers(self, obj):
        return AutoSalonStatsService.get_special_customers()

    def get_car_price(self, obj):
        return AutoSalonStatsService.get_car_price()

    def get_sale_history_count(self, obj):
        return AutoSalonStatsService.get_sale_history_count()

    def get_prices_in_sale_histories(self, obj):
        return AutoSalonStatsService.get_prices_in_sale_histories()


class SupplierStatsSerializer(ModelSerializer):
    """
    Serializer for SupplierStatsViewSet
    """

    total_prices = SerializerMethodField()
    autosalons_count = SerializerMethodField()
    cars_count = SerializerMethodField()
    sale_history_count = SerializerMethodField()
    prices_in_sale_histories = SerializerMethodField()

    class Meta:
        model = Supplier
        fields = (
            "total_prices",
            "autosalons_count",
            "cars_count",
            "sale_history_count",
            "prices_in_sale_histories",
        )

    def get_total_prices(self, obj):
        return SupplierStatsService.get_total_prices()

    def get_autosalons_count(self, obj):
        return SupplierStatsService.get_autosalons_count()

    def get_cars_count(self, obj):
        return SupplierStatsService.get_cars_count()

    def get_sale_history_count(self, obj):
        return SupplierStatsService.get_sale_history_count()

    def get_prices_in_sale_histories(self, obj):
        return SupplierStatsService.get_prices_in_sale_histories()
