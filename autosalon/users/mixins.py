from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response

from .models import Customer

from .serializers import CustomerStatsSerializer


class CustomerStatsMixin(ListModelMixin, GenericAPIView):
    """
    Mixin for AutoSalonStatsViewSet
    """

    queryset = Customer.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = CustomerStatsSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
