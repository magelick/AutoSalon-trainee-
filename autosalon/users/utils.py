import os
from datetime import datetime, timedelta

from passlib.context import CryptContext
import jwt

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
