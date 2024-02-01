from rest_framework import viewsets

from .serializers import MeterSerializer, MeterCreateSerializer, MeterUpdateSerializer
from .models import Meter


class MeterViewSet(viewsets.ModelViewSet):
    queryset = Meter.objects.all()

    def get_serializer_class(self):
        if self.action in ('update', 'partial_update'):
            return MeterUpdateSerializer
        elif self.action in ('create', ):
            return MeterCreateSerializer
        return MeterSerializer
