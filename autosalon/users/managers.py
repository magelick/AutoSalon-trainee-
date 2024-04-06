from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class CustomerQuerySet(models.QuerySet):
    """
    QuerySet for CustomManager
    """

    def autosalons(self):
        return self.prefetch_related("autosalons")


class CustomManager(BaseUserManager):
    """
    Custom Class Manager for Customer's model
    """

    def get_queryset(self):
        return CustomerQuerySet(model=self.model, using=self._db)

    def autosalons(self):
        return self.get_queryset().autosalons()

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


class SaleHistoryOfCustomerQuerySet(models.QuerySet):
    """
    QuerySet for SpecialOfferOfSupplierManager
    """

    def customer(self):
        return self.select_related("customer")

    def car(self):
        return self.select_related("car")


class SaleHistoryOfCustomerManager(models.Manager):
    """
    Manager for SaleHistoryOfCustomer's model
    """

    def get_queryset(self):
        return SaleHistoryOfCustomerQuerySet(model=self.model, using=self._db)

    def customer(self):
        return self.get_queryset().customer()

    def car(self):
        return self.get_queryset().car()
