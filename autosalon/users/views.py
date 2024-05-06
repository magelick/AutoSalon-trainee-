from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Customer, SaleHistoryOfCustomer

from .filters import CustomerFilter, SaleHistoryOfCustomerFilter

from .tasks import send_confirmation_email

from .serializers import (
    CustomerSerializer,
    SaleHistoryOfCustomerSerializer,
    LoginSerializer,
    TokenSerializer,
    PasswordSerializer,
    EmailSerializer,
    CustomerStatsSerializer,
)

from .utils import (
    create_hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    verify_refresh_token,
)

from api.views import ViewSetCache

from .mixins import CustomerStatsMixin

from .permissions import IsAdminPermission, IsManagerPermission, IsCustomerPermission


@extend_schema_view(
    list=extend_schema(
        summary="List of Customers",
        description="Get list of all Customers",
        tags=["Customer"],
    ),
    create=extend_schema(
        summary="New Customer", description="Create new Customer", tags=["Customer"]
    ),
    retrieve=extend_schema(
        summary="Get Customer", description="Get Customer by id", tags=["Customer"]
    ),
    update=extend_schema(
        summary="Update Customer",
        description="Update Customer by id",
        tags=["Customer"],
    ),
    partial_update=extend_schema(
        summary="Partial update Customer",
        description="Partial update Customer by id",
        tags=["Customer"],
    ),
    destroy=extend_schema(
        summary="Delete Customer",
        description="Delete Customer by id",
        tags=["Customer"],
    ),
)
class CustomerViewSet(ModelViewSet):
    """
    ViewSet for Customer model
    """

    permission_classes = [IsManagerPermission, IsAdminPermission]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filterset_class = CustomerFilter
    filter_backends = (DjangoFilterBackend,)


@extend_schema_view(
    list=extend_schema(
        summary="List of Sale Histories Of Customer",
        description="Get list of all Sale Histories Of Customer",
        tags=["Sale History Of Customer"],
    ),
    create=extend_schema(
        summary="New Sale History Of Customer",
        description="Create new Sale History Of Customer",
        tags=["Sale History Of Customer"],
    ),
    retrieve=extend_schema(
        summary="Get Sale History Of Customer",
        description="Get Sale History Of Customer by id",
        tags=["Sale History Of Customer"],
    ),
    update=extend_schema(
        summary="Update Sale History Of Customer",
        description="Update Sale History Of Customer by id",
        tags=["Sale History Of Customer"],
    ),
    partial_update=extend_schema(
        summary="Partial update Sale History Of Customer",
        description="Partial update Sale History Of Customer by id",
        tags=["Sale History Of Customer"],
    ),
    destroy=extend_schema(
        summary="Delete Sale History Of Customer",
        description="Delete Sale History Of Customer by id",
        tags=["Sale History Of Customer"],
    ),
)
class SaleHistoryOfCustomerViewSet(ViewSetCache):
    """
    ViewSet for SaleHistoryOfCustomer model
    """

    permission_classes = [IsManagerPermission, IsAdminPermission]
    serializer_class = SaleHistoryOfCustomerSerializer
    queryset = SaleHistoryOfCustomer.objects.all()
    filterset_class = SaleHistoryOfCustomerFilter
    filter_backends = (DjangoFilterBackend,)


@extend_schema(tags=["Auth"])
class RegisterViewSet(CreateModelMixin, GenericViewSet):
    """
    ViewSet for register customer
    """

    permission_classes = [AllowAny]
    serializer_class = CustomerSerializer

    def get_queryset(self):
        pass

    @extend_schema(summary="Register Customer")
    def create(self, request, *args, **kwargs):
        """
        Registration user
        :param request:
        :return:
        """
        # validated all request data
        serializer = CustomerSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            # if admin try register
            if serializer["username"] == "admin":
                Customer.objects.create_superuser(
                    email=serializer.validated_data["email"],
                    password=serializer.validated_data["password"],
                )
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

        # hashing validate password and save changes
        serializer.validated_data["password"] = create_hash_password(
            password=serializer.validated_data["password"]
        )
        serializer.save()
        # create tokens
        access_token = create_access_token(sub=serializer.validated_data["email"])
        refresh_token = create_refresh_token(sub=serializer.validated_data["email"])
        # confirmation email
        send_confirmation_email.delay(email=serializer.validated_data["email"])
        # return Response with all instances
        return Response(
            {
                "customer": serializer.data,
                "access_token": access_token,
                "refresh_token": refresh_token,
            },
            status=status.HTTP_201_CREATED,
        )


@extend_schema(tags=["Auth"])
class LoginViewSet(CreateModelMixin, GenericViewSet):
    """
    ViewSet for login customer
    """

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def get_queryset(self):
        pass

    @extend_schema(summary="Login Customer")
    def create(self, request, *args, **kwargs):
        """
        Login user
        :param request:
        :return:
        """
        # take email and password
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

        # get customer by email
        customer = get_object_or_404(Customer, email=serializer.validated_data["email"])
        # check of password by verification
        if not verify_password(
            serializer.validated_data["password"], customer.password
        ):
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


@extend_schema(tags=["Auth"])
class UpdateTokenViewSet(CreateModelMixin, GenericViewSet):
    """
    ViewSet for update access token
    """

    permission_classes = [IsAuthenticated]
    serializer_class = TokenSerializer

    def get_queryset(self):
        pass

    @extend_schema(summary="Update Access token")
    def create(self, request, *args, **kwargs):
        """
        Update token
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # take refresh_token
        serializer = TokenSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

        # refresh token verification
        refresh_token = verify_refresh_token(
            refresh_token=serializer.validated_data["refresh_token"]
        )
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


@extend_schema(tags=["Auth"])
class PasswordUpdateViewSet(CreateModelMixin, GenericViewSet):
    """
    ViewSet for update customer password
    """

    permission_classes = [IsAuthenticated]
    serializer_class = PasswordSerializer

    def get_queryset(self):
        pass

    @extend_schema(summary="Update Password")
    def create(self, request, *args, **kwargs):
        """
        Password user update
        :param request:
        :return:
        """
        # take email and password
        serializer = PasswordSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

        # get customer by email
        customer = get_object_or_404(Customer, email=serializer.validated_data["email"])
        # create new password for customer
        update_password = create_hash_password(
            password=serializer.validated_data["new_password"]
        )
        # changing and saving new customer password
        customer.password = update_password
        customer.save()
        # confirmation email
        send_confirmation_email.delay(email=customer.email)
        # return Response
        return Response(
            {"password": "Password succesfuly updated"}, status=status.HTTP_201_CREATED
        )


@extend_schema(tags=["Auth"])
class EmailUpdateViewSet(CreateModelMixin, GenericViewSet):
    """
    ViewSet for update customer email
    """

    permission_classes = [IsAuthenticated]
    serializer_class = EmailSerializer

    def get_queryset(self):
        pass

    @extend_schema(summary="Update Email")
    def create(self, request, *args, **kwargs):
        """
        Password user update
        :param request:
        :return:
        """
        # take email and new email
        serializer = EmailSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
        # get customer by email
        customer = get_object_or_404(Customer, email=serializer.validated_data["email"])
        # update customer email on new email
        customer.email = serializer.validated_data["new_email"]
        customer.save()
        # confirmation email
        send_confirmation_email.delay(customer.email)
        # return Response
        return Response(
            {"email": "Email succesfuly updated"}, status=status.HTTP_201_CREATED
        )


@extend_schema(tags=["Stats"])
@extend_schema_view(
    list=extend_schema(
        summary="List of Customer stats",
        description="Get list of all customer stats",
    )
)
class CustomerStatsViewSet(CustomerStatsMixin, GenericViewSet):
    """
    StatsViewSet for Customer's model
    """

    permission_classes = [IsManagerPermission, IsAdminPermission, IsCustomerPermission]

    def list(self, request, *args, **kwargs):
        serializer = CustomerStatsSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
