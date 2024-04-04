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
        self.customer = G(
            Customer,
            username="admin",
            first_name="Vladimir",
            last_name="Zhirinovsky",
            email="zhirikpushka@gmail.com",
            password="russiatop!",
            balance=100000.00,
        )
        self.customer2 = G(
            Customer,
            username="customer",
            first_name="Ksenia",
            last_name="Sobchak",
            email="sobchakrulit@gmail.com",
            password="yarygonnablow!(",
            balance=10000.00,
        )

        self.client.force_authenticate(self.customer, self.customer2)

    def test_customer_list(self):
        response = self.client.get(path=reverse(viewname="customers-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = CustomerSerializer(
            [self.customer, self.customer2], many=True
        ).data
        serializer_first_names = [item.get("first_name") for item in serializer_data]
        response_first_names = [item.get("first_name") for item in response.data]

        self.assertEqual(response_first_names, serializer_first_names)

    def test_customer_create(self):
        data = {
            "username": "manager",
            "first_name": "Cristiano",
            "last_name": "Ronaldo",
            "email": "sooocris@gmail.com",
            "password": "supergool!!))",
            "balance": 999999.00,
        }
        response = self.client.post(path=reverse("customers-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_customer_retrieve(self):
        response = self.client.get(
            path=reverse(viewname="customers-detail", args=[self.customer.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = CustomerSerializer(self.customer).data
        serializer_first_name = serializer_data.get("first_name")
        response_first_name = response.data.get("first_name")

        self.assertEqual(response_first_name, serializer_first_name)

    def test_customer_update(self):
        data = {
            "username": "customer",
            "first_name": "Cristiano",
            "last_name": "Ronaldo",
            "email": "sooocris@gmail.com",
            "password": "supergool!!))",
            "balance": 999999.00,
        }
        response = self.client.put(
            path=reverse(viewname="customers-detail", args=[self.customer.id]),
            data=data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        customer = Customer.instances.get(first_name="Cristiano")
        self.assertEqual(customer.first_name, "Cristiano")

    def test_customer_destroy(self):
        response = self.client.delete(
            path=reverse(viewname="customers-detail", args=[self.customer.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Customer.instances.filter(first_name="Vladimir").exists())


class SaleHistoryOfCustomerTestCase(APITestCase):
    """
    APITestCase for SaleHistoryOfCustomerViewSet
    """

    def setUp(self):
        self.customer1 = G(
            Customer,
            username="admin",
            first_name="Vladimir",
            last_name="Zhirinovsky",
            email="zhirikpushka@gmail.com",
            password="russiatop!",
            balance=100000.00,
        )
        self.car = G(model=Car, model_name="Volkswagen Arteon")

        self.sale_history1 = G(
            SaleHistoryOfCustomer,
            customer=self.customer1,
            car=self.car,
            price=85000.00,
            date=timezone.now(),
        )
        self.sale_history2 = G(
            SaleHistoryOfCustomer,
            customer=self.customer1,
            car=self.car,
            price=45000.00,
            date=timezone.now(),
        )

        self.client.force_authenticate(self.customer1)

    def test_sale_history_of_customer_list(self):
        response = self.client.get(path=reverse(viewname="history_customers-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SaleHistoryOfCustomerSerializer(
            [self.sale_history1, self.sale_history2], many=True
        ).data
        serializer_prices = [item.get("price") for item in serializer_data]
        response_prices = [item.get("price") for item in response.data]

        self.assertEqual(response_prices, serializer_prices)

    def test_sale_history_fo_customer_create(self):
        data = {
            "customer": self.customer1.id,
            "car": self.car.id,
            "price": 35000.00,
            "date": timezone.now(),
        }
        response = self.client.post(
            path=reverse(viewname="history_customers-list"), data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_sale_history_fo_customer_retrieve(self):
        response = self.client.get(
            path=reverse(
                viewname="history_customers-detail", args=[self.sale_history1.id]
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SaleHistoryOfCustomerSerializer(self.sale_history1).data
        serializer_price = serializer_data.get("price")
        response_price = response.data.get("price")

        self.assertEqual(response_price, serializer_price)

    def test_sale_history_fo_customer_update(self):
        data = {
            "customer": self.customer1.id,
            "car": self.car.id,
            "price": 135000.00,
            "date": timezone.now(),
        }
        response = self.client.put(
            path=reverse(
                viewname="history_customers-detail", args=[self.sale_history2.id]
            ),
            data=data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RegisterTestCase(APITestCase):
    """
    APITestCase for RegisterViewSet
    """

    def test_register(self):
        data1 = {
            "username": "customer",
            "first_name": "Cristiano",
            "last_name": "Ronaldo",
            "email": "sooocris@gmail.com",
            "password": "supergool!!))",
            "balance": 999999.00,
        }
        data2 = {
            "username": "customer",
            "first_name": "Lionel",
            "last_name": "Messi",
            "email": "muchugraciasmessi@gmail.com",
            "password": "goat!!))",
            "balance": 999999.00,
        }

        response1 = self.client.post(path=reverse(viewname="register-list"), data=data1)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        response2 = self.client.post(path=reverse(viewname="register-list"), data=data2)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)


class LoginTestCase(APITestCase):
    """
    APITestCase for LoginViewSet
    """

    def setUp(self):
        data1 = {
            "username": "customer",
            "first_name": "Cristiano",
            "last_name": "Ronaldo",
            "email": "sooocris@gmail.com",
            "password": "supergool!!))",
            "balance": 999999.00,
        }
        self.customer = self.client.post(
            path=reverse(viewname="register-list"), data=data1
        )

    def test_login(self):
        data = {
            "email": "sooocris@gmail.com",
            "password": "supergool!!))",
        }
        response = self.client.post(path=reverse(viewname="login-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateTokenTestCase(APITestCase):
    """
    APITestCase for UpdateTokenViewSet
    """

    def setUp(self):
        self.customer1 = G(
            Customer,
            username="admin",
            first_name="Vladimir",
            last_name="Zhirinovsky",
            email="zhirikpushka@gmail.com",
            password="russiatop!",
            balance=100000.00,
        )

    def test_update_token(self):
        refresh_token = {"refresh_token": create_refresh_token(sub=self.customer1.id)}
        response = self.client.post(
            path=reverse(viewname="update_token-list"), data=refresh_token
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
