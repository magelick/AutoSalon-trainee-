import datetime

from django.test import TestCase
from django_dynamic_fixture import G, F

from ..models import Customer, SaleHistoryOfCustomer


class CustomerTestCase(TestCase):
    """
    TestCase of Customer's model
    """

    def test_customer_username(self):
        """
        Test of check username's value
        :return:
        """
        customer = G(Customer, username="Customer")
        self.assertEqual(customer.username, "Customer")
        self.assertNotEqual(customer.username, "Manager")
        self.assertNotEqual(customer.username, "Admin")

    def test_customer_first_name(self):
        """
        Test of check first_name's value
        :return:
        """
        customer = G(Customer, first_name="Vasya")
        self.assertEqual(customer.first_name, "Vasya")
        self.assertNotEqual(customer.first_name, "Petya")

    def test_customer_last_name(self):
        """
        Test of check last_name's value
        :return:
        """
        customer = G(Customer, last_name="Pupkin")
        self.assertEqual(customer.last_name, "Pupkin")
        self.assertNotEqual(customer.last_name, "Mishkin")

    def test_customer_email(self):
        """
        Test of check email's value
        :return:
        """
        customer = G(Customer, email="vasya228@gmail.com")
        self.assertEqual(customer.email, "vasya228@gmail.com")
        self.assertNotEqual(customer.email, "vasya328@gmail.com")

    def test_customer_password(self):
        """
        Test of check password's value
        :return:
        """
        customer = G(Customer, password="qwerty123456!@#$")
        self.assertEqual(customer.password, "qwerty123456!@#$")
        self.assertNotEqual(customer.password, "qwerty123456!@#")
        self.assertNotEqual(customer.password, "qwerty123456")

    def test_customer_balance(self):
        """
        Test of check balance's value
        :return:
        """
        customer = G(Customer, balance=10000.0)
        self.assertEqual(customer.balance, 10000.0)
        self.assertNotEqual(customer.balance, 120000.0)


class SaleHistoryOfCustomerTestCase(TestCase):
    """
    TestCase of Customer's model
    """

    def test_sale_history_of_customer_customer(self):
        """
        Test of check customer's value
        :return:
        """
        sale_history = G(
            SaleHistoryOfCustomer, customer=F(username="Customer", first_name="Vasya")
        )
        self.assertEqual(sale_history.customer.username, "Customer")
        self.assertNotEqual(sale_history.customer.username, "Admin")
        self.assertEqual(sale_history.customer.first_name, "Vasya")
        self.assertNotEqual(sale_history.customer.first_name, "Misha")

    def test_sale_history_of_customer_car(self):
        """
        Test of check car's value
        :return:
        """
        sale_history = G(SaleHistoryOfCustomer, car=F(model_name="BMW M5 G30"))
        self.assertEqual(sale_history.car.model_name, "BMW M5 G30")
        self.assertNotEqual(sale_history.car.model_name, "AUDI RS6 C8")

    def test_sale_history_of_customer_price(self):
        """
        Test of check price's value
        :return:
        """
        sale_history = G(SaleHistoryOfCustomer, price=95000.0)
        self.assertEqual(sale_history.price, 95000.0)
        self.assertNotEqual(sale_history.price, 195000.0)

    def test_sale_history_of_customer_date(self):
        """
        Test of check date's value
        :return:
        """
        sale_history = G(SaleHistoryOfCustomer, date=datetime.date(2023, 2, 10))
        self.assertEqual(sale_history.date, datetime.date(2023, 2, 10))
        self.assertNotEqual(sale_history.date, datetime.date(2022, 3, 15))
