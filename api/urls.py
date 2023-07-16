from user.views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("members", MemberView)

urlpatterns = [
    path("", include(router.urls))
]