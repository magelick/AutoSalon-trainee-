from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Customer, SaleHistoryOfCustomer

from .serializers import (
    CustomerSerializer,
    SaleHistoryOfCustomerSerializer,
    LoginSerializer,
    TokenSerializer,
)

from .utils import (
    create_hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    verify_refresh_token,
)


class CustomerViewSet(ModelViewSet):
    """
    ViewSet for Customer model
    """

    permission_classes = [IsAuthenticated]

    serializer_class = CustomerSerializer
    queryset = Customer.instances.all()


class SaleHistoryOfCustomerViewSet(ModelViewSet):
    """
    ViewSet for SaleHistoryOfCustomer model
    """
    permission_classes = [IsAuthenticated]

    serializer_class = SaleHistoryOfCustomerSerializer
    queryset = SaleHistoryOfCustomer.objects.select_related("customer", "car").all()


class RegisterViewSet(ModelViewSet):
    """
    ViewSet for register customer
    """

    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        """
        Registration user
        :param request:
        :return:
        """
        # validated all request data
        serializer = CustomerSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

        # hashing validate password and save changes
        serializer.validated_data["password"] = create_hash_password(
            password=serializer.validated_data["password"]
        )
        serializer.save()
        # create tokens
        access_token = create_access_token(sub=serializer.validated_data["email"])
        refresh_token = create_refresh_token(sub=serializer.validated_data["email"])
        # return Response with all instances
        return Response(
            {
                "customer": serializer.data,
                "access_token": access_token,
                "refresh_token": refresh_token,
            },
            status=status.HTTP_201_CREATED,
        )


class LoginViewSet(ModelViewSet):
    """
    ViewSet for login customer
    """

    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        """
        Login user
        :param request:
        :return:
        """
        # take email and password
        email = request.data["email"]
        password = request.data["password"]
        # check for mail and password existence
        if not email:
            return Response("Email wasn't declared", status=status.HTTP_403_FORBIDDEN)
        if not password:
            return Response("Password wasn't declared")
        # get customer by email
        customer = get_object_or_404(Customer, email=email)
        # check of password by verification
        if not verify_password(password, customer.password):
            return Response(
                {"password": "Invalid password"}, status=status.HTTP_403_FORBIDDEN
            )
        # create tokens
        access_token = create_access_token(sub=customer.email)
        refresh_token = create_refresh_token(sub=customer.email)
        # return Response with all instances
        return Response(
            {"access_token": access_token, "refresh_token": refresh_token},
            status=status.HTTP_201_CREATED,
        )


class UpdateTokenViewSet(ModelViewSet):
    """
    ViewSet for update access token
    """

    serializer_class = TokenSerializer

    def create(self, request, *args, **kwargs):
        """
        Update token
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # take refresh_token
        token = request.data["refresh_token"]
        # check for token existence
        if not token:
            return Response(
                {"refresh_token": "Token not found"}, status=status.HTTP_403_FORBIDDEN
            )
        # refresh token verification
        refresh_token = verify_refresh_token(refresh_token=token)
        if refresh_token is False:
            return Response(
                {"refresh_token": "Invalid refresh token"},
                status=status.HTTP_403_FORBIDDEN,
            )
        # take sub for refresh_token
        customer_email = refresh_token["sub"]
        # create access token with refresh token sub
        access_token = create_access_token(sub=customer_email)
        # return Response with new access token
        return Response({"access_token": access_token}, status=status.HTTP_201_CREATED)
