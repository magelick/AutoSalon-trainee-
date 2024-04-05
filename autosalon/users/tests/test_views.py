from django.urls import reverse
from django.utils import timezone
from django_dynamic_fixture import G
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Customer, SaleHistoryOfCustomer
from api.models import Car
from ..serializers import CustomerSerializer, SaleHistoryOfCustomerSerializer
from ..utils import create_refresh_token


class CustomerTestCase(APITestCase):
    """
    APITestCase for CustomerViewSet
    """

    def setUp(self):
        self.first_customer = G(
            Customer,
            username="admin",
            first_name="Vladimir",
            last_name="Zhirinovsky",
            email="zhirikpushka@gmail.com",
            password="russiatop!",
            balance=100000.00,
        )
        self.second_customer = G(
            Customer,
            username="customer",
            first_name="Ksenia",
            last_name="Sobchak",
            email="sobchakrulit@gmail.com",
            password="yarygonnablow!(",
            balance=10000.00,
        )
        self.customer_data = {
            "username": "manager",
            "first_name": "Cristiano",
            "last_name": "Ronaldo",
            "email": "sooocris@gmail.com",
            "password": "supergool!!))",
            "balance": 999999.00,
        }

        self.client.force_authenticate(self.first_customer, self.second_customer)

    def test_customer_list(self):
        response = self.client.get(path=reverse(viewname="customers-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = CustomerSerializer(
            [self.first_customer, self.second_customer], many=True
        ).data
        serializer_first_names = [item.get("first_name") for item in serializer_data]
        response_first_names = [item.get("first_name") for item in response.data]

        self.assertEqual(response_first_names, serializer_first_names)

    def test_customer_create(self):
        response = self.client.post(
            path=reverse("customers-list"), data=self.customer_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_customer_retrieve(self):
        response = self.client.get(
            path=reverse(viewname="customers-detail", args=[self.first_customer.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = CustomerSerializer(self.first_customer).data
        serializer_first_name = serializer_data.get("first_name")
        response_first_name = response.data.get("first_name")

        self.assertEqual(response_first_name, serializer_first_name)

    def test_customer_update(self):
        response = self.client.put(
            path=reverse(viewname="customers-detail", args=[self.first_customer.id]),
            data=self.customer_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        customer = Customer.instances.get(first_name="Cristiano")
        self.assertEqual(customer.first_name, "Cristiano")

    def test_customer_destroy(self):
        response = self.client.delete(
            path=reverse(viewname="customers-detail", args=[self.first_customer.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Customer.instances.filter(first_name="Vladimir").exists())


class SaleHistoryOfCustomerTestCase(APITestCase):
    """
    APITestCase for SaleHistoryOfCustomerViewSet
    """

    def setUp(self):
        self.customer = G(
            Customer,
            username="admin",
            first_name="Vladimir",
            last_name="Zhirinovsky",
            email="zhirikpushka@gmail.com",
            password="russiatop!",
            balance=100000.00,
        )
        self.car = G(model=Car, model_name="Volkswagen Arteon")

        self.first_sale_history = G(
            SaleHistoryOfCustomer,
            customer=self.customer,
            car=self.car,
            price=85000.00,
            date=timezone.now(),
        )
        self.second_sale_history = G(
            SaleHistoryOfCustomer,
            customer=self.customer,
            car=self.car,
            price=45000.00,
            date=timezone.now(),
        )
        self.sale_history_data = {
            "customer": self.customer.id,
            "car": self.car.id,
            "price": 35000.00,
            "date": timezone.now(),
        }

        self.client.force_authenticate(self.customer)

    def test_sale_history_of_customer_list(self):
        response = self.client.get(path=reverse(viewname="history_customers-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SaleHistoryOfCustomerSerializer(
            [self.first_sale_history, self.second_sale_history], many=True
        ).data
        serializer_prices = [item.get("price") for item in serializer_data]
        response_prices = [item.get("price") for item in response.data]

        self.assertEqual(response_prices, serializer_prices)

    def test_sale_history_fo_customer_create(self):
        response = self.client.post(
            path=reverse(viewname="history_customers-list"), data=self.sale_history_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_sale_history_fo_customer_retrieve(self):
        response = self.client.get(
            path=reverse(
                viewname="history_customers-detail", args=[self.first_sale_history.id]
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SaleHistoryOfCustomerSerializer(self.first_sale_history).data
        serializer_price = serializer_data.get("price")
        response_price = response.data.get("price")

        self.assertEqual(response_price, serializer_price)

    def test_sale_history_fo_customer_update(self):
        response = self.client.put(
            path=reverse(
                viewname="history_customers-detail", args=[self.second_sale_history.id]
            ),
            data=self.sale_history_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RegisterTestCase(APITestCase):
    """
    APITestCase for RegisterViewSet
    """

    def setUp(self):
        self.first_data = {
            "username": "customer",
            "first_name": "Cristiano",
            "last_name": "Ronaldo",
            "email": "sooocris@gmail.com",
            "password": "supergool!!))",
            "balance": 999999.00,
        }
        self.second_data = {
            "username": "customer",
            "first_name": "Lionel",
            "last_name": "Messi",
            "email": "muchugraciasmessi@gmail.com",
            "password": "goat!!))",
            "balance": 999999.00,
        }

    def test_register(self):
        first_response = self.client.post(
            path=reverse(viewname="register-list"), data=self.first_data
        )
        self.assertEqual(first_response.status_code, status.HTTP_201_CREATED)
        second_response = self.client.post(
            path=reverse(viewname="register-list"), data=self.second_data
        )
        self.assertEqual(second_response.status_code, status.HTTP_201_CREATED)


class LoginTestCase(APITestCase):
    """
    APITestCase for LoginViewSet
    """

    def setUp(self):
        self.register_data = {
            "username": "customer",
            "first_name": "Cristiano",
            "last_name": "Ronaldo",
            "email": "sooocris@gmail.com",
            "password": "supergool!!))",
            "balance": 999999.00,
        }
        self.customer = self.client.post(
            path=reverse(viewname="register-list"), data=self.register_data
        )
        self.login_data = {
            "email": "sooocris@gmail.com",
            "password": "supergool!!))",
        }

    def test_login(self):
        response = self.client.post(
            path=reverse(viewname="login-list"), data=self.login_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateTokenTestCase(APITestCase):
    """
    APITestCase for UpdateTokenViewSet
    """

    def setUp(self):
        self.first_customer = G(
            Customer,
            username="admin",
            first_name="Vladimir",
            last_name="Zhirinovsky",
            email="zhirikpushka@gmail.com",
            password="russiatop!",
            balance=100000.00,
        )

        self.refresh_token = {
            "refresh_token": create_refresh_token(sub=self.first_customer.id)
        }

    def test_update_token(self):
        response = self.client.post(
            path=reverse(viewname="update_token-list"), data=self.refresh_token
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
