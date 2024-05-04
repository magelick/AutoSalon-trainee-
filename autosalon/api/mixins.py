from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from .models import AutoSalon, Supplier


class AutoSalonStatsMixin(ListModelMixin, GenericAPIView):
    """
    Mixin for AutoSalonStatsViewSet
    """

    queryset = AutoSalon.objects.all()


class SupplierStatsMixin(ListModelMixin, GenericAPIView):
    """
    Mixin for AutoSalonStatsViewSet
    """

    queryset = Supplier.objects.all()
