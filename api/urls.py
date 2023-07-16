from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import *
from shipping_address.views import *
from customer.views import *

router = DefaultRouter()
router.register("members", MemberView)
router.register("customers", Customer_View)
router.register("shipping_addresses", Shipping_Address_View)

urlpatterns = [
    path("", include(router.urls))
]