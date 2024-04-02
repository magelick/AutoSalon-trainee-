from rest_framework.serializers import ModelSerializer, Serializer, CharField

from .models import Customer, SaleHistoryOfCustomer


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
