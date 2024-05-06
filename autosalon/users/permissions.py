from rest_framework import permissions


class IsAdminPermission(permissions.IsAdminUser):
    """
    Permission class for Customer's model instance, in which username is 'customer'
    """

    def has_permission(self, request, view):
        if request.user.username == "admin":
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.username == "admin":
            return True
        else:
            return False


class IsManagerPermission(permissions.IsAuthenticated):
    """
    Permission class for Customer's model instance, in which username is 'customer'
    """

    def has_permission(self, request, view):
        if request.user.username == "manager":
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.username == "manager":
            return True
        else:
            return False


class IsCustomerPermission(permissions.BasePermission):
    """
    Permission class for Customer's model instance, in which username is 'customer'
    """

    def has_permission(self, request, view):
        if request.user.username == "customer":
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.username == "customer":
            return True
        else:
            return False
