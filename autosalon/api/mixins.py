from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from .models import AutoSalon, Supplier
from .serializers import AutoSalonStatsSerializer, SupplierStatsSerializer


class AutoSalonStatsMixin(ListModelMixin, GenericAPIView):
    """
    Mixin for AutoSalonStatsViewSet
    """

    queryset = AutoSalon.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = AutoSalonStatsSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SupplierStatsMixin(ListModelMixin, GenericAPIView):
    """
    Mixin for AutoSalonStatsViewSet
    """

    queryset = Supplier.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = SupplierStatsSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
