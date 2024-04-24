from rest_framework.fields import CharField
from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    Serializer,
)

from .models import Customer, SaleHistoryOfCustomer

from .utils import CustomerStatsService


class CustomerSerializer(ModelSerializer):
    """
    Serializer for Customer model
    """

    class Meta:
        model = Customer
        fields = ("username", "first_name", "last_name", "email", "password", "balance")
        extra_kwargs = {"password": {"write_only": True}}


class LoginSerializer(ModelSerializer):
    """
    Serializer for Login of Customer model
    """

    class Meta:
        model = Customer
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}


class SaleHistoryOfCustomerSerializer(ModelSerializer):
    """
    Serializer for SaleHistoryOfCustomer model
    """

    class Meta:
        model = SaleHistoryOfCustomer
        fields = "__all__"


class TokenSerializer(Serializer):
    """
    Serializer for Token
    """

    # token field
    refresh_token = CharField()

    class Meta:
        fields = ("refresh_token",)


class CustomerStatsSerializer(ModelSerializer):
    """
    Serializer for CustomerStatsViewSet
    """

    admin_count = IntegerField(read_only=True)
    manager_count = IntegerField(read_only=True)
    customer_count = IntegerField(read_only=True)
    email_count = IntegerField(read_only=True)
    total_balance = IntegerField(read_only=True)
    autosalons_count = IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = (
            "admin_count",
            "manager_count",
            "customer_count",
            "email_count",
            "total_balance",
            "autosalons_count",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["admin_count"] = CustomerStatsService.get_admin_count()
        data["manager_count"] = CustomerStatsService.get_manager_count()
        data["customer_count"] = CustomerStatsService.get_customer_count()
        data["email_count"] = CustomerStatsService.get_email_count()
        data["total_balance"] = CustomerStatsService.get_total_balance()
        data["autosalons_count"] = CustomerStatsService.get_autosalons_count()

        return data
