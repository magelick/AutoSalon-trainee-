from rest_framework.viewsets import ModelViewSet

from .models import Customer, SaleHistoryOfCustomer

from .serializers import CustomerSerializer, SaleHistoryOfCustomerSerializer


class CustomerViewSet(ModelViewSet):
    """
    ViewSet for Customer model
    """

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class SaleHistoryOfCustomerViewSet(ModelViewSet):
    """
    ViewSet for SaleHistoryOfCustomer model
    """

    serializer_class = SaleHistoryOfCustomerSerializer
    queryset = SaleHistoryOfCustomer.objects.select_related("customer", "car").all()
