from rest_framework.serializers import ModelSerializer

from .models import Customer, SaleHistoryOfCustomer


class CustomerSerializer(ModelSerializer):
    """
    Serializer for Customer model
    """

    class Meta:
        model = Customer
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class SaleHistoryOfCustomerSerializer(ModelSerializer):
    """
    Serializer for SaleHistoryOfCustomer model
    """

    class Meta:
        model = SaleHistoryOfCustomer
        fields = "__all__"
