from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from .models import Customer


class CustomerStatsMixin(ListModelMixin, GenericAPIView):
    """
    Mixin for AutoSalonStatsViewSet
    """

    queryset = Customer.objects.all()
