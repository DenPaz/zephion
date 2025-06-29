from rest_framework import serializers

from apps.sensors.models import SensorReading


class SensorReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorReading
        fields = [
            "id",
            "timestamp",
            "temperature",
            "humidity",
            "gas_value",
        ]
        read_only_fields = [
            "id",
            "timestamp",
        ]
