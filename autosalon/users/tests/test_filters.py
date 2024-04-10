import pytest

from ..filters import CustomerFilter, SaleHistoryOfCustomerFilter


@pytest.mark.django_db
def test_customer_username(customer_object):
    data = {"username": "admin"}
    filter_data = CustomerFilter(data=data)
    assert filter_data.qs.first().username == customer_object.username


@pytest.mark.django_db
def test_customer_first_name(customer_object):
    data = {"first_name": "Vladimir"}
    filter_data = CustomerFilter(data=data)
    assert filter_data.qs.first().first_name == customer_object.first_name


@pytest.mark.django_db
def test_customer_last_name(customer_object):
    data = {"last_name": "Zhirinovsky"}
    filter_data = CustomerFilter(data=data)
    assert filter_data.qs.first().last_name == customer_object.last_name


@pytest.mark.django_db
def test_customer_email(customer_object):
    data = {"email": "zhirikpushka@gmail.com"}
    filter_data = CustomerFilter(data=data)
    assert filter_data.qs.first().email == customer_object.email


@pytest.mark.django_db
def test_customer_balance(customer_object):
    data = {"balance": 100000.00}
    filter_data = CustomerFilter(data=data)
    assert filter_data.qs.first().balance == customer_object.balance


@pytest.mark.django_db
def test_sale_history_of_customer_customer(
    sale_history_of_customer_object, customer_object
):
    data = {"customer__first_name": customer_object.first_name}
    filter_data = SaleHistoryOfCustomerFilter(data=data)
    assert filter_data.qs.first().customer == sale_history_of_customer_object.customer


@pytest.mark.django_db
def test_sale_history_of_customer_car(
    sale_history_of_customer_object, second_car_object
):
    data = {"car__model_name": second_car_object.model_name}
    filter_data = SaleHistoryOfCustomerFilter(data=data)
    assert filter_data.qs.first().car == sale_history_of_customer_object.car


@pytest.mark.django_db
def test_sale_history_of_customer_price(sale_history_of_customer_object):
    data = {"price": 85000.00}
    filter_data = SaleHistoryOfCustomerFilter(data=data)
    assert filter_data.qs.first().price == sale_history_of_customer_object.price


@pytest.mark.django_db
def test_sale_history_of_customer_date(sale_history_of_customer_object):
    data = {"date": str(sale_history_of_customer_object.date.year)}
    filter_data = SaleHistoryOfCustomerFilter(data=data)
    assert filter_data.qs.first().date == sale_history_of_customer_object.date
