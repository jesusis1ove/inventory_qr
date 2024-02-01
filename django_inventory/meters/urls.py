from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import MeterViewSet

router = DefaultRouter()
router.register(r'', MeterViewSet, basename='meters')

urlpatterns = router.urls
