from django.db import models
from django_countries import fields

from .managers import (
    AutoSalonManager,
    CarManager,
    OptionCarManager,
    SupplierManager,
    SaleHistoryManager,
    SpecialOfferOfAutoSalonManager,
    SpecialOfferOfSupplierManager,
)


class AutoSalon(models.Model):
    """
    Model of Autosalon
    """

    objects = AutoSalonManager()
    # name
    name: models.CharField = models.CharField(
        max_length=128, blank=False, null=False, verbose_name="Name of Autosalon"
    )
    # location
    location: fields.CountryField = fields.CountryField(
        max_length=128, blank=False, null=False, verbose_name="Location of Autosalon"
    )
    # balance
    balance: models.DecimalField = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=False,
        verbose_name="Balance of Autosalon",
    )
    # is active instance
    is_active: models.BooleanField = models.BooleanField(
        default=True, verbose_name="Flag is active"
    )
    # suppliers
    suppliers: models.ManyToManyField = models.ManyToManyField(
        to="Supplier",
        related_name="autosalons",
        blank=True,
        verbose_name="Suppliers of AutoSalon",
    )
    # customers
    customers: models.ManyToManyField = models.ManyToManyField(
        to="users.Customer",
        related_name="autosalons",
        blank=True,
        verbose_name="Customers of AutoSalon",
    )

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = "autosalon"
        verbose_name_plural = "autosalons"
        app_label = "api"


class Car(models.Model):
    """
    Model of Car
    """

    objects = CarManager()
    # model
    model_name: models.CharField = models.CharField(
        max_length=128, blank=False, null=False, verbose_name="Model of Car"
    )
    # autosalons
    autosalons: models.ManyToManyField = models.ManyToManyField(
        to="AutoSalon",
        related_name="cars",
        blank=True,
        verbose_name="Autosalons with Car",
    )
    # options
    options: models.ManyToManyField = models.ManyToManyField(
        to="OptionCar",
        related_name="cars_options",
        blank=True,
        verbose_name="Options of Car",
    )
    # is active instance
    is_active: models.BooleanField = models.BooleanField(
        default=True, verbose_name="Flag is active"
    )

    def __repr__(self):
        return self.model_name

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"


class OptionCar(models.Model):
    """
    Class of Options for Car
    """

    objects = OptionCarManager()
    # year
    year: models.DateField = models.DateField(
        blank=False, null=False, verbose_name="Year of car"
    )
    # mileage
    mileage: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=False, null=False, verbose_name="Mileage of Car"
    )
    # body type
    body_type: models.CharField = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        choices=[
            ("sedan", "Sedan"),
            ("coupe", "Coupe"),
            ("hatchback", "Hatchback"),
            ("pickup", "Pickup"),
            ("off-road", "Off-road"),
            ("sport", "Sport"),
            ("hyper", "Hyper"),
            ("suv", "SUV"),
            ("crossover", "Crossover"),
            ("minivan", "Minivan"),
            ("convertible", "Сonvertible"),
            ("universal", "Universal"),
        ],
        verbose_name="Body type of Car",
    )
    # transmission type
    transmission_type: models.CharField = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        choices=[("automatic", "Automatic"), ("mechanics", "Mechanic")],
        verbose_name="Transmission type of Car",
    )
    # drive unit type
    drive_unit_type: models.CharField = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        choices=[("complete", "Complete"), ("front", "Front"), ("back", "Back")],
        verbose_name="Drive unit type of Car",
    )
    # color
    color: models.CharField = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        choices=[
            ("red", "Red"),
            ("blue", "Blue"),
            ("green", "Green"),
            ("orange", "Orange"),
            ("yellow", "Yellow"),
            ("violet", "Violet"),
            ("brown", "Brown"),
            ("black", "Black"),
            ("grey", "Grey"),
            ("white", "White"),
            ("pink", "Pink"),
        ],
        verbose_name="Color of Car",
    )
    # engine type
    engine_type: models.CharField = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        choices=[("petrol", "Petrol"), ("diesel", "Diesel"), ("electro", "Electro")],
        verbose_name="Engine type of Car",
    )
    # cars
    cars: models.ManyToManyField = models.ManyToManyField(
        to="Car",
        related_name="options_car",
        blank=True,
        verbose_name="Cars with Option",
    )

    def __repr__(self):
        return self.color

    class Meta:
        verbose_name = "option of car"
        verbose_name_plural = "options of car"


class Supplier(models.Model):
    """
    Class of Supplier
    """

    objects = SupplierManager()
    # name
    name: models.CharField = models.CharField(
        max_length=128, blank=False, null=False, verbose_name="Name of Supplier"
    )
    # year of issue
    year_of_issue: models.DateField = models.DateField(
        blank=False, null=False, verbose_name="Year for issue of Supplier"
    )
    # price of each cars
    price: models.DecimalField = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name="Price of each cars",
    )
    # cars, which have supplier
    cars: models.ManyToManyField = models.ManyToManyField(
        to="Car",
        related_name="suppliers_of_car",
        blank=True,
        verbose_name="Cars, which have Supplier",
    )
    # is active instance
    is_active: models.BooleanField = models.BooleanField(
        default=True, verbose_name="Flag is active"
    )

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = "supplier"
        verbose_name_plural = "suppliers"
        app_label = "api"


class SaleHistory(models.Model):
    """
    Class of Sale History between AutoSalons and Suppliers
    """

    objects = SaleHistoryManager()
    # autosalon
    autosalon: models.ForeignKey = models.ForeignKey(
        to="AutoSalon",
        on_delete=models.CASCADE,
        related_name="sale_history",
        blank=False,
        null=False,
        verbose_name="AutoSalon of Sale History",
    )
    # supplier
    supplier: models.ForeignKey = models.ForeignKey(
        to="Supplier",
        on_delete=models.CASCADE,
        related_name="sale_history",
        blank=False,
        null=False,
        verbose_name="Supplier of Sale History",
    )
    # price
    price: models.DecimalField = models.DecimalField(
        default=0.0,
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name="Price of Sale History",
    )

    def __repr__(self):
        return self.price

    class Meta:
        verbose_name = "sale history"
        verbose_name_plural = "sale histories"


class SpecialOfferOfAutoSalon(models.Model):
    """
    Class of special offer
    """

    objects = SpecialOfferOfAutoSalonManager()
    # name
    name: models.CharField = models.CharField(
        max_length=64, blank=False, null=False, verbose_name="Name of Special Offer"
    )
    # description
    descr: models.TextField = models.TextField(
        blank=False, null=False, verbose_name="Description of Special Offer"
    )
    # discount
    discount: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=False, null=False, verbose_name="Discount of Special Offer"
    )
    # dealer
    dealer: models.ForeignKey = models.ForeignKey(
        to="AutoSalon",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="AutoSalon of that Special Offer",
    )
    # start date
    start_date: models.DateField = models.DateField(
        auto_now_add=True,
        blank=False,
        null=False,
        verbose_name="Start date of Special Offer",
    )
    # end date
    end_date: models.DateField = models.DateField(
        blank=True, null=False, verbose_name="End date of Special Offer"
    )
    # is active instance
    is_active: models.BooleanField = models.BooleanField(
        default=True, verbose_name="Flag is active"
    )

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = "special offer of autosalon"
        verbose_name_plural = "special offers of autosalons"


class SpecialOfferOfSupplier(models.Model):
    """
    Class of special offer
    """

    objects = SpecialOfferOfSupplierManager()
    # name
    name: models.CharField = models.CharField(
        max_length=64, blank=False, null=False, verbose_name="Name of Special Offer"
    )
    # description
    descr: models.TextField = models.TextField(
        blank=False, null=False, verbose_name="Description of Special Offer"
    )
    # discount
    discount: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=False, null=False, verbose_name="Discount of Special Offer"
    )
    # supplier
    supplier: models.ForeignKey = models.ForeignKey(
        to="Supplier",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Supplier of that Special Offer",
    )
    # start date
    start_date: models.DateField = models.DateField(
        auto_now_add=True,
        blank=False,
        null=False,
        verbose_name="Start date of Special Offer",
    )
    # end date
    end_date: models.DateField = models.DateField(
        blank=True, null=False, verbose_name="End date of Special Offer"
    )
    # is active instance
    is_active: models.BooleanField = models.BooleanField(
        default=True, verbose_name="Flag is active"
    )

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = "special offer of supplier"
        verbose_name_plural = "special offers of suppliers"
