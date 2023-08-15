from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertisementViewSet

router = DefaultRouter()
router.register(r"adv", AdvertisementViewSet)

urlpatterns = [path("api/", include(router.urls))]
