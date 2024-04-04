from django.db import models


class AutoSalonQuerySet(models.QuerySet):
    """
    QuerySet for AutoSalonManager
    """

    def suppliers(self):
        return self.prefetch_related("suppliers")

    def customers(self):
        return self.prefetch_related("customers")

    def sale_history(self):
        return self.prefetch_related("sale_history")

    def cars(self):
        return self.prefetch_related("cars")


class AutoSalonManager(models.Manager):
    """
    Manager for AutoSalon's model
    """

    def get_queryset(self):
        return AutoSalonQuerySet(model=self.model, using=self._db)

    def suppliers(self):
        return self.get_queryset().suppliers()

    def customers(self):
        return self.get_queryset().customers()

    def sale_history(self):
        return self.get_queryset().sale_history()

    def cars(self):
        return self.get_queryset().cars()


class CarQuerySet(models.QuerySet):
    """
    QuerySet for CarManager
    """

    def autosalons(self):
        return self.prefetch_related("autosalons")

    def options(self):
        return self.prefetch_related("options")

    def suppliers_of_car(self):
        return self.prefetch_related("suppliers_of_car")


class CarManager(models.Manager):
    """
    Manager for Car's model
    """

    def get_queryset(self):
        return CarQuerySet(model=self.model, using=self._db)

    def autosalons(self):
        return self.get_queryset().autosalons()

    def options(self):
        return self.get_queryset().options()

    def suppliers_of_car(self):
        return self.get_queryset().suppliers_of_car()


class OptionCarQuerySet(models.QuerySet):
    """
    QuerySet for OptionCarManager
    """

    def sedan(self):
        return self.filter(body_type="sedan")

    def coupe(self):
        return self.filter(body_type="coupe")

    def hatchback(self):
        return self.filter(body_type="hatchback")

    def pickup(self):
        return self.filter(body_type="pickup")

    def off_road(self):
        return self.filter(body_type="off-road")

    def sport(self):
        return self.filter(body_type="sport")

    def hyper(self):
        return self.filter(body_type="hyper")

    def suv(self):
        return self.filter(body_type="suv")

    def crossover(self):
        return self.filter(body_type="crossover")

    def minivan(self):
        return self.filter(body_type="minivan")

    def convertible(self):
        return self.filter(body_type="convertible")

    def universal(self):
        return self.filter(body_type="universal")

    def automatic_transmission_type(self):
        return self.filter(transmission_type="automatic")

    def mechanics_transmission_type(self):
        return self.filter(transmission_type="mechanics")

    def complete_drive_unite_type(self):
        return self.filter(drive_unit_type="complete")

    def front_drive_unite_type(self):
        return self.filter(drive_unit_type="front")

    def back_drive_unite_type(self):
        return self.filter(drive_unit_type="back")

    def red_color(self):
        return self.filter(color="red")

    def blue_color(self):
        return self.filter(color="blue")

    def green_color(self):
        return self.filter(color="green")

    def orange_color(self):
        return self.filter(color="orange")

    def yellow_color(self):
        return self.filter(color="yellow")

    def violet_color(self):
        return self.filter(color="violet")

    def brown_color(self):
        return self.filter(color="brown")

    def black_color(self):
        return self.filter(color="black")

    def grey_color(self):
        return self.filter(color="grey")

    def white_color(self):
        return self.filter(color="white")

    def pink_color(self):
        return self.filter(color="pink")

    def petrol_engine_type(self):
        return self.filter(engine_type="petrol")

    def diesel_engine_type(self):
        return self.filter(engine_type="diesel")

    def electro_engine_type(self):
        return self.filter(engine_type="electro")

    def cars(self):
        return self.prefetch_related("cars")


class OptionCarManager(models.Manager):
    """
    Manager for OptionCar's model
    """

    def get_queryset(self):
        return OptionCarQuerySet(model=self.model, using=self._db)

    def sedan(self):
        return self.get_queryset().sedan()

    def coupe(self):
        return self.get_queryset().coupe()

    def hatchback(self):
        return self.get_queryset().hatchback()

    def pickup(self):
        return self.get_queryset().pickup()

    def off_road(self):
        return self.get_queryset().off_road()

    def sport(self):
        return self.get_queryset().sport()

    def hyper(self):
        return self.get_queryset().hyper()

    def suv(self):
        return self.get_queryset().suv()

    def crossover(self):
        return self.get_queryset().crossover()

    def minivan(self):
        return self.get_queryset().minivan()

    def convertible(self):
        return self.get_queryset().convertible()

    def universal(self):
        return self.get_queryset().universal()

    def automatic_transmission_type(self):
        return self.get_queryset().automatic_transmission_type()

    def mechanics_transmission_type(self):
        return self.get_queryset().mechanics_transmission_type()

    def complete_drive_unite_type(self):
        return self.get_queryset().complete_drive_unite_type()

    def front_drive_unite_type(self):
        return self.get_queryset().front_drive_unite_type()

    def back_drive_unite_type(self):
        return self.get_queryset().back_drive_unite_type()

    def red_color(self):
        return self.get_queryset().red_color()

    def blue_color(self):
        return self.get_queryset().blue_color()

    def green_color(self):
        return self.get_queryset().green_color()

    def orange_color(self):
        return self.get_queryset().orange_color()

    def yellow_color(self):
        return self.get_queryset().yellow_color()

    def violet_color(self):
        return self.get_queryset().violet_color()

    def brown_color(self):
        return self.get_queryset().brown_color()

    def black_color(self):
        return self.get_queryset().black_color()

    def grey_color(self):
        return self.get_queryset().grey_color()

    def white_color(self):
        return self.get_queryset().white_color()

    def pink_color(self):
        return self.get_queryset().pink_color()

    def petrol_engine_type(self):
        return self.get_queryset().petrol_engine_type()

    def diesel_engine_type(self):
        return self.get_queryset().diesel_engine_type()

    def electro_engine_type(self):
        return self.get_queryset().electro_engine_type()

    def cars(self):
        return self.get_queryset().cars()


class SupplierQuerySet(models.QuerySet):
    """
    QuerySet for SupplierManager
    """

    def cars(self):
        return self.prefetch_related("cars")

    def autosalons(self):
        return self.prefetch_related("autosalons")

    def sale_history(self):
        return self.prefetch_related("sale_history")


class SupplierManager(models.Manager):
    """
    manager for Supplier's model
    """

    def get_queryset(self):
        return SupplierQuerySet(model=self.model, using=self._db)

    def cars(self):
        return self.get_queryset().cars()

    def autosalon(self):
        return self.get_queryset().autosalons()

    def sale_history(self):
        return self.get_queryset().sale_history()


class SaleHistoryQuerySet(models.QuerySet):
    """
    QuerySet for SaleHistoryManager
    """

    def autosalon(self):
        return self.select_related("autosalon")

    def supplier(self):
        return self.select_related("supplier")


class SaleHistoryManager(models.Manager):
    """
    QuerySet for SaleHistory's model
    """

    def get_queryset(self):
        return SaleHistoryQuerySet(model=self.model, using=self._db)

    def autosalon(self):
        return self.get_queryset().autosalon()

    def supplier(self):
        return self.get_queryset().supplier()


class SpecialOfferOfAutoSalonQuerySet(models.QuerySet):
    """
    QuerySet for SpecialOfferOfAutoSalonManager
    """

    def dealer(self):
        return self.select_related("dealer")


class SpecialOfferOfAutoSalonManager(models.Manager):
    """
    Manager for SpecialOfferOfAutoSalon's model
    """

    def get_queryset(self):
        return SpecialOfferOfAutoSalonQuerySet(model=self.model, using=self._db)

    def dealer(self):
        return self.get_queryset().dealer()


class SpecialOfferOfSupplierQuerySet(models.QuerySet):
    """
    QuerySet for SpecialOfferOfSupplierManager
    """

    def supplier(self):
        return self.select_related("supplier")


class SpecialOfferOfSupplierManager(models.Manager):
    """
    Manager for SpecialOfferOfSupplier's model
    """

    def get_queryset(self):
        return SpecialOfferOfSupplierQuerySet(model=self.model, using=self._db)

    def supplier(self):
        return self.get_queryset().supplier()
