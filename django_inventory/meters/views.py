from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import MeterSerializer, MeterCreateSerializer, MeterUpdateSerializer
from .models import Meter


class MeterViewSet(viewsets.ModelViewSet):
    queryset = Meter.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_serializer_class(self):
        if self.action in ('update', 'partial_update'):
            return MeterUpdateSerializer
        elif self.action in ('create', ):
            return MeterCreateSerializer
        return MeterSerializer

    @action(detail=True, url_path='qr', methods=['get'])
    def get_qr(self, request, pk):
        qrcode = Meter.objects.get(pk=pk).get_qrcode()
        response = HttpResponse(qrcode)
        response['Content-Type'] = "image/png"
        response['Cache-Control'] = "max-age=0"
        return response
