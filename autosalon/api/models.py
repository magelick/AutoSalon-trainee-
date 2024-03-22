from django.db import models


class AutoSalon(models.Model):
    """
    Model of Autosalon
    """
    # name
    name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        verbose_name="Name of Autosalon"
    )
    # location
    location = fields.CountryField(
        max_length=128,
        blank=False,
        null=False,
        verbose_name="Location of Autosalon"
    )
    # balance
    balance = models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=False,
        verbose_name="Balance of Autosalon"
    )
    # is active instance
    is_active = models.BooleanField(
        default=True,
        verbose_name="Flag is active"
    )
    # suppliers
    suppliers = models.ManyToManyField(
        to="Customer",
        blank=False,
        null=False,
        verbose_name="Suppliers of AutoSalon"
    )
    # customers
    customers = models.ManyToManyField(
        to="Customer",
        blank=False,
        null=False,
        verbose_name="Customers of AutoSalon"
    )
    # counter of car
    counter_of_car = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Counter of Car"
    )

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = "autosalon"
        verbose_name_plural = "autosalons"


class Car(models.Model):
    """
    Model of Car
    """
    # model
    model = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        verbose_name="Model of Car"
    )
    # autosalons
    autosalons = models.ManyToManyField(
        to="AutoSalon",
        related_name="cars",
        blank=False,
        null=False,
        verbose_name="Autosalons with Car"
    )
    # options
    options = models.ManyToManyField(
        to="OptionCar",
        related_name="cars",
        blank=False,
        null=False,
        verbose_name="Options of Car"
    )
    # is active instance
    is_active = models.BooleanField(
        default=True,
        verbose_name="Flag is active"
    )

    def __repr__(self):
        return self.model

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"


class OptionCar(models.Model):
    """
    Class of Options for Car
    """
    # year
    year = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name="Year of car"
    )
    # mileage
    mileage = models.PositiveIntegerField(
        blank=False,
        null=False,
        verbose_name="Mileage of Car"
    )
    # body type
    body_type = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        verbose_name="Body type of Car"
    )
    # transmission type
    transmission_type = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        verbose_name="Transmission type of Car"
    )
    # drive unit type
    drive_unit_type = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        verbose_name="Drive unit type of Car"
    )
    # color
    color = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        verbose_name="Color of Car"
    )
    # engine type
    engine_type = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        verbose_name="Engine type of Car"
    )
    # cars
    cars = models.ManyToManyField(
        to="Car",
        related_name="options",
        blank=False,
        null=False,
        verbose_name="Cars with Option"
    )
    # is active instance
    is_active = models.BooleanField(
        default=True,
        verbose_name="Flag is active"
    )

    class Meta:
        verbose_name = "option of car"
        verbose_name_plural = "options of car"


class Supplier(models.Model):
    """
    Class of Supplier
    """
    # name
    name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        verbose_name="Name of Supplier"
    )
    # year of issue
    year_of_issue = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name="Year for issue of Supplier"
    )
    # price of each cars
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name="Price of each cars"
    )
    # cars, which have supplier
    cars = models.ManyToManyField(
        to="Car",
        related_name="suppliers",
        blank=False,
        null=False,
        verbose_name="Cars, which have Supplier"
    )
    # is active instance
    is_active = models.BooleanField(
        default=True,
        verbose_name="Flag is active"
    )

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = "supplier"
        verbose_name_plural = "suppliers"


class SaleHistory(models.Model):
    """
    Class of Sale History between AutoSalons and Suppliers
    """
    # autosalon
    autosalon = models.ForeignKey(
        to="AutoSalon",
        on_delete=models.CASCADE,
        related_name="sale_history",
        blank=False,
        null=False,
        verbose_name="AutoSalon of Sale History"
    )
    # supplier
    supplier = models.ForeignKey(
        to="Supplier",
        on_delete=models.CASCADE,
        related_name="sale_history",
        blank=False,
        null=False,
        verbose_name="Supplier of Sale History"
    )
    # price
    price = models.DecimalField(
        default=0.0,
        max_digits=8,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name="Price of Sale History"
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
    # name
    name = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        verbose_name="Name of Special Offer"
    )
    # description
    descr = models.TextField(
        blank=False,
        null=False,
        verbose_name="Description of Special Offer"
    )
    # discount
    discount = models.PositiveIntegerField(
        blank=False,
        null=False,
        verbose_name="Discount of Special Offer"
    )
    # dealer
    dealer = models.ForeignKey(
        to="AutoSalon",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="AutoSalon of that Special Offer"
    )
    # start date
    start_date = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        verbose_name="Start date of Special Offer"
    )
    # end date
    end_date = models.DateTimeField(
        blank=True,
        null=False,
        verbose_name="End date of Special Offer"
    )
    # is active instance
    is_active = models.BooleanField(
        default=True,
        verbose_name="Flag is active"
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
    # name
    name = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        verbose_name="Name of Special Offer"
    )
    # description
    descr = models.TextField(
        blank=False,
        null=False,
        verbose_name="Description of Special Offer"
    )
    # discount
    discount = models.PositiveIntegerField(
        blank=False,
        null=False,
        verbose_name="Discount of Special Offer"
    )
    # supplier
    supplier = models.ForeignKey(
        to="Supplier",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Supplier of that Special Offer"
    )
    # is active instance
    is_active = models.BooleanField(
        default=True,
        verbose_name="Flag is active"
    )

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = "special offer of supplier"
        verbose_name_plural = "special offers of suppliers"
