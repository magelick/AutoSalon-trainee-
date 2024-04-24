import os
from datetime import datetime, timedelta

from django.db.models import Count, Sum
from passlib.context import CryptContext
import jwt

from .models import Customer

# create CryptoContext instance with supplement bcrypt
pwd_context = CryptContext(schemes=["bcrypt"])


def create_hash_password(password: str) -> str:
    """
    Create hash password
    :param password:
    :return:
    """
    return pwd_context.hash(password)


def verify_password(password: str, hash_password: str) -> bool:
    """
    Verify password with hash password
    :param password:
    :param hash_password:
    :return:
    """
    return pwd_context.verify(password, hash_password)


def create_access_token(sub: int) -> str:
    """
    Create access token
    :param sub:
    :return:
    """
    return jwt.encode(
        payload={
            "sub": sub,
            "exp": datetime.now() + timedelta(minutes=30),
        },
        key=os.getenv("SECRET_KEY_OF_ACCESS_TOKEN"),
        algorithm=os.getenv("ALGORITHM"),
    )


def verify_access_token(access_token: str):
    """
    Verify access token with treating JWTErrors
    :param access_token:
    :return:
    """
    return jwt.decode(
        access_token,
        os.getenv("SECRET_KEY_OF_ACCESS_TOKEN"),
        algorithms=["HS256"],
    )


def create_refresh_token(sub: int) -> str:
    """
    Create refresh token
    :param sub:
    :return:
    """
    return jwt.encode(
        payload={
            "sub": sub,
            "exp": datetime.now() + timedelta(minutes=60),
        },
        key=os.getenv("REFRESH_TOKEN_EXPIRE"),
        algorithm=os.getenv("ALGORITHM"),
    )


def verify_refresh_token(refresh_token: str):
    """
    Verify refresh token with treating JWTErrors
    :param refresh_token:
    :return:
    """
    return jwt.decode(
        refresh_token,
        os.getenv("REFRESH_TOKEN_EXPIRE"),
        algorithms=["HS256"],
    )


class CustomerStatsService:
    """
    MixinService for CustomerStatsMixin
    """

    @staticmethod
    def get_admin_count():
        return (
            Customer.objects.annotate(admin_count=Count("username", distinct=True))
            .filter(username="admin")
            .values("admin_count", "email")
            .count()
        )

    @staticmethod
    def get_manager_count():
        return (
            Customer.objects.annotate(manager_count=Count("username", distinct=True))
            .filter(username="manager")
            .values("manager_count", "email")
            .count()
        )

    @staticmethod
    def get_customer_count():
        return (
            Customer.objects.annotate(customer_count=Count("username", distinct=True))
            .filter(username="customer")
            .values("customer_count", "email")
            .count()
        )

    @staticmethod
    def get_email_count():
        return Customer.objects.annotate(
            email_count=Count("email", distinct=True)
        ).values("email", "email_count")

    @staticmethod
    def get_total_balance():
        return Customer.objects.annotate(total_balance=Sum("balance")).values(
            "email", "total_balance"
        )

    @staticmethod
    def get_autosalons_count():
        return Customer.objects.annotate(
            autosalons_count=Count("autosalons", distinct=True)
        ).values("email", "autosalons_count")
