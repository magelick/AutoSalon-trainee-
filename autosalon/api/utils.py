from django.db.models import Count, Sum, Min, Max

from .models import AutoSalon, Supplier


class AutoSalonStatsService:
    """
    MixinService for AutoSalonStatsMixin
    """

    @staticmethod
    def get_suppliers_count():
        return AutoSalon.objects.annotate(
            suppliers_count=Count("suppliers", distinct=True)
        ).values("name", "suppliers_count")

    @staticmethod
    def get_cars_count():
        return AutoSalon.objects.annotate(cars_count=Count("cars")).values(
            "name", "cars_count"
        )

    @staticmethod
    def get_total_price():
        return AutoSalon.objects.annotate(total_price=Sum("balance")).values(
            "name", "total_price"
        )

    @staticmethod
    def get_special_customers():
        return AutoSalon.objects.annotate(
            special_customers=Count("customers", distinct=True)
        ).values("name", "special_customers")

    @staticmethod
    def get_car_price():
        return AutoSalon.objects.annotate(
            max_price=Max("suppliers__price"), min_price=Min("suppliers__price")
        ).values("name", "max_price", "min_price")

    @staticmethod
    def get_sale_history_count():
        return AutoSalon.objects.annotate(
            sale_histories=Count("sale_history", distinct=True)
        ).values("name", "sale_histories")

    @staticmethod
    def get_prices_in_sale_histories():
        return AutoSalon.objects.annotate(
            max_price_in_history=Max("sale_history__price"),
            min_price_in_history=Min("sale_history__price"),
        ).values("name", "max_price_in_history", "min_price_in_history")


class SupplierStatsService:
    """
    MixinService for SupplierStatsMixin
    """

    @staticmethod
    def get_total_prices():
        return Supplier.objects.annotate(
            max_price=Max("price"), min_price=Min("price")
        ).values("name", "max_price", "min_price")

    @staticmethod
    def get_autosalons_count():
        return Supplier.objects.annotate(
            autosalons_count=Count("autosalons", distinct=True)
        ).values("name", "autosalons_count")

    @staticmethod
    def get_cars_count():
        return Supplier.objects.annotate(
            cars_count=Count("cars", distinct=True)
        ).values("name", "cars_count")

    @staticmethod
    def get_sale_history_count():
        return Supplier.objects.annotate(
            sale_histories_count=Count("sale_history", distinct=True)
        ).values("name", "sale_histories_count")

    @staticmethod
    def get_prices_in_sale_histories():
        return Supplier.objects.annotate(
            max_price_in_history=Max("sale_history__price"),
            min_price_in_history=Min("sale_history__price"),
        ).values("name", "max_price_in_history", "min_price_in_history")
