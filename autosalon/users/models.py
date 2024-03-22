from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    """
    Class of Customer
    """
    # username
    username = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        verbose_name="Username of Customer"
    )
    # first name
    first_name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        verbose_name="First name of Customer"
    )
    # last name
    last_name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        verbose_name="Last name of Customer"
    )
    # email
    email = models.EmailField(
        blank=False,
        null=False,
        verbose_name="Email of Customer"
    )
    # password
    password = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        verbose_name="Password of Customer"
    )
    # balance
    balance = models.DecimalField(
        default=0.0,
        max_digits=8,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name="Balance of Customer"
    )

    def __repr__(self):
        return self.username

    class Meta:
        verbose_name = "customer"
        verbose_name_plural = "customers"


class SaleHistoryOfCustomer(models.Model):
    """
    Class of Sale History for Customer
    """
    # customer
    customer = models.ForeignKey(
        to="Customer",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Customer"
    )
    # car
    car = models.ForeignKey(
        to="Car",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Car"
    )
    # price
    price = models.DecimalField(
        default=0.0,
        max_digits=2,
        decimal_places=8,
        blank=False,
        null=False,
        verbose_name="Price"
    )
    # date of deal
    date = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        verbose_name="Date of deal"
    )

    def __repr__(self):
        return self.price

    class Meta:
        verbose_name = "sale history"
        verbose_name_plural = "sale histories"