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
