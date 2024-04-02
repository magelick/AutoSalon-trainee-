from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class CustomManager(BaseUserManager):
    """
    Custom Class Manager
    """

    def create_customer(
        self, username, email, password, first_name, last_name, balance=0.0
    ):
        """
        Method of create customer
        :param username:
        :param email:
        :param password:
        :param first_name:
        :param last_name:
        :param balance:
        :return:
        """
        if not email:
            raise ValueError("Customers must have an email")

        customer = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            balance=balance,
        )

        customer.set_password(password)
        customer.save(using=self._db)
        return customer

    def create_superuser(
        self,
        email,
        password,
        username="admin",
        first_name="admin",
        last_name="admin",
        balance=0.0,
    ):
        """
        Method of create superuser
        :param email:
        :param password:
        :param username:
        :param first_name:
        :param last_name:
        :param balance:
        :return:
        """
        customer = self.create_customer(
            username, email, password, first_name, last_name, balance
        )
        customer.username = "admin"
        customer.is_staff = True
        customer.is_superuser = True
        customer.save(using=self._db)
        return customer


class Customer(AbstractUser):
    """
    Class of Customer
    """

    # username
    username: models.CharField = models.CharField(
        default="customer",
        max_length=64,
        choices=[("admin", "Admin"), ("manager", "Manager"), ("customer", "Customer")],
        blank=False,
        null=False,
        unique=False,
        verbose_name="Username of Customer",
    )
    # first name
    first_name: models.CharField = models.CharField(
        max_length=128, blank=False, null=False, verbose_name="First name of Customer"
    )
    # last name
    last_name: models.CharField = models.CharField(
        max_length=128, blank=False, null=False, verbose_name="Last name of Customer"
    )
    # email
    email: models.EmailField = models.EmailField(
        blank=False, null=False, unique=True, verbose_name="Email of Customer"
    )
    # password
    password: models.CharField = models.CharField(
        max_length=128, blank=False, null=False, verbose_name="Password of Customer"
    )
    # balance
    balance: models.DecimalField = models.DecimalField(
        default=0.0, max_digits=8, decimal_places=2, verbose_name="Balance of Customer"
    )
    # use CustomManager as usual manager for Customer model
    instances = CustomManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]

    def clean(self):
        """
        Check password on special symbols
        :return:
        """
        # Special symbols, which one or more from this should be in password
        special_symbols = "!@#$%^&*()-_+=[]{}|:;<>,.?/~"
        # If the password contains one or more special symbols
        if special_symbols in self.password:
            # return validate password
            return
        # Else other case - raise ValidationError with message
        raise ValidationError(
            message="Password must contain at least one special symbol"
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
    customer: models.ForeignKey = models.ForeignKey(
        to="Customer",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Customer",
    )
    # car
    car: models.ForeignKey = models.ForeignKey(
        to="api.Car",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Car",
    )
    # price
    price: models.DecimalField = models.DecimalField(
        default=0.0,
        max_digits=8,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name="Price of Sale History",
    )
    # date of deal
    date: models.DateTimeField = models.DateTimeField(
        auto_now_add=True, blank=False, null=False, verbose_name="Date of deal"
    )

    def __repr__(self):
        return self.price

    class Meta:
        verbose_name = "sale history"
        verbose_name_plural = "sale histories"
