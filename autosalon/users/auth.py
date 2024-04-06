import jwt
from drf_spectacular.extensions import OpenApiAuthenticationExtension

from .models import Customer

from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from .utils import verify_access_token


class JWTAuthentication(BaseAuthentication):
    """
    Base class for check of JWT-Authentication
    """

    def authenticate(self, request):
        """
        Function of authenticate user in system
        :param request:
        :return:
        """
        # pull out Authorization from query params
        token_param = request.headers.get("Authorization", None)

        # if Authorization is None...
        if token_param is None:
            # ...return none
            return None

        # pull out access token by getting rid of the signature
        token = token_param.replace("Bearer ", "")

        try:
            # try verify access token
            payload = verify_access_token(access_token=token)
            # pull out user.id from payload
            email_user = payload["sub"]
            # and get User by id
            user = Customer.objects.filter(email=email_user).first()

            # if user is found ...
            if user is not None:
                # ...return user with verify access token
                return (user, token)

            # if user is not found, return None
            return None

        # processing ExpiredSignatureError...
        except jwt.ExpiredSignatureError:
            # ...get message error
            raise exceptions.AuthenticationFailed("Token has expired")
        # processing InvalidTokenError...
        except jwt.InvalidTokenError:
            # ...get message error
            raise exceptions.AuthenticationFailed("Invalid token")

    def authenticate_header(self, request):
        """
        Function of header for authenticate_header
        :param request:
        :return:
        """
        # return signature Bearer
        return "Bearer"


class JWTAuthenticationExtension(OpenApiAuthenticationExtension):
    """
    Extension class for JWTAuthentication in Swagger
    """

    name = "JWTAuth"
    target_class = JWTAuthentication

    def get_security_definition(self, auto_schema):
        return {"type": "apiKey", "in": "header", "name": "Authorization"}
