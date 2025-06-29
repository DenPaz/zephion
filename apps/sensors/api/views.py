from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.sensors.models import SensorReading

from .serializers import SensorReadingSerializer


class SensorReadingViewSet(viewsets.ModelViewSet):
    queryset = SensorReading.objects.all().order_by("-timestamp")
    serializer_class = SensorReadingSerializer

    @action(detail=False, methods=["get"])
    def latest(self, request):
        latest_reading = self.queryset.first()
        if latest_reading:
            serializer = self.get_serializer(latest_reading)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "No sensor readings found."},
            status=status.HTTP_404_NOT_FOUND,
        )
