from rest_framework import viewsets

from .serializers import MeterSerializer
from .models import Meter


class MeterViewSet(viewsets.ModelViewSet):
    queryset = Meter.objects.all()

    def get_serializer_class(self):
        return MeterSerializer
