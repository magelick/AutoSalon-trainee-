from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Customer, SaleHistoryOfCustomer

from .filters import CustomerFilter, SaleHistoryOfCustomerFilter

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

    permission_classes = [IsAuthenticated]

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
class SaleHistoryOfCustomerViewSet(ModelViewSet):
    """
    ViewSet for SaleHistoryOfCustomer model
    """

    permission_classes = [IsAuthenticated]

    serializer_class = SaleHistoryOfCustomerSerializer
    queryset = SaleHistoryOfCustomer.objects.all()
    filterset_class = SaleHistoryOfCustomerFilter
    filter_backends = (DjangoFilterBackend,)


@extend_schema(tags=["Auth"])
class RegisterViewSet(ModelViewSet):
    """
    ViewSet for register customer
    """

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


@extend_schema(tags=["Auth"])
class LoginViewSet(ModelViewSet):
    """
    ViewSet for login customer
    """

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


@extend_schema(tags=["Auth"])
class UpdateTokenViewSet(ModelViewSet):
    """
    ViewSet for update access token
    """

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


@extend_schema(tags=["Stats"])
@extend_schema_view(
    list=extend_schema(
        summary="List of Supplier stats",
        description="Get list of all supplier stats",
        tags=["Supplier stats"],
    )
)
class CustomerStatsViewSet(ModelViewSet):
    """
    StatsViewSet for Customer's model
    """

    serializer_class = CustomerSerializer

    def list(self, request, *args, **kwargs):
        # Get list customers with count admins
        admin_count = (
            Customer.objects.annotate(admin_count=Count("username", distinct=True))
            .filter(username="admin")
            .values("admin_count", "email")
        )
        # Get list customers with count managers
        manager_count = (
            Customer.objects.annotate(manager_count=Count("username", distinct=True))
            .filter(username="manager")
            .values("manager_count", "email")
        )
        # Get list customers with count empty customers
        customer_count = (
            Customer.objects.annotate(customer_count=Count("username", distinct=True))
            .filter(username="customer")
            .values("customer_count", "email")
        )
        # Get list customers with count their emails
        email_count = Customer.objects.annotate(
            email_count=Count("email", distinct=True)
        )
        # Get list customers with their total balance
        total_balance = Customer.objects.annotate(total_balance=Sum("balance")).values(
            "email", "total_balance"
        )
        # Get list customers with count their autosalons
        autosalons_count = Customer.objects.annotate(
            autosalons_count=Count("autosalons", distinct=True)
        ).values("email", "autosalons_count")
        # Define serializers
        admin_count_serializer = CustomerSerializer(admin_count, many=True).data
        manager_count_serializer = CustomerSerializer(manager_count, many=True).data
        customer_count_serializer = CustomerSerializer(customer_count, many=True).data
        email_count_serializer = CustomerSerializer(email_count, many=True).data
        total_balance_serializer = CustomerSerializer(total_balance, many=True).data
        autosalons_count_serializer = CustomerSerializer(
            autosalons_count, many=True
        ).data
        # Define reponse data
        response_data = {
            "admin_count": admin_count_serializer,
            "manager_count": manager_count_serializer,
            "customer_count": customer_count_serializer,
            "email_count": email_count_serializer,
            "total_balance": total_balance_serializer,
            "autosalons_count": autosalons_count_serializer,
        }
        # return Response
        return Response(response_data, status=status.HTTP_200_OK)

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
