from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CustomerViewSet,
    SaleHistoryOfCustomerViewSet,
    RegisterViewSet,
    LoginViewSet,
    UpdateTokenViewSet,
)

# initial default router
router = DefaultRouter()
# connect viewsets with router
router.register(prefix="customers", viewset=CustomerViewSet)
router.register(prefix="sale_histories", viewset=SaleHistoryOfCustomerViewSet)


urlpatterns = [
    path("v1/", include(router.urls)),
    path("register/", RegisterViewSet.as_view({"post": "create"})),
    path("login/", LoginViewSet.as_view({"post": "create"})),
    path("update_token/", UpdateTokenViewSet.as_view({"post": "create"})),
]
