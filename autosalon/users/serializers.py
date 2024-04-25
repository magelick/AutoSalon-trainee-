from rest_framework.fields import CharField, SerializerMethodField
from rest_framework.serializers import (
    ModelSerializer,
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

    admin_count = SerializerMethodField()
    manager_count = SerializerMethodField()
    customer_count = SerializerMethodField()
    email_count = SerializerMethodField()
    total_balance = SerializerMethodField()
    autosalons_count = SerializerMethodField()

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

    def get_admin_count(self, obj):
        return CustomerStatsService.get_admin_count()

    def get_manager_count(self, obj):
        return CustomerStatsService.get_manager_count()

    def get_customer_count(self, obj):
        return CustomerStatsService.get_customer_count()

    def get_email_count(self, obj):
        return CustomerStatsService.get_email_count()

    def get_total_balance(self, obj):
        return CustomerStatsService.get_total_balance()

    def get_autosalons_count(self, obj):
        return CustomerStatsService.get_autosalons_count()
