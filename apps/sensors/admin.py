from django.contrib import admin

from .models import SensorReading


@admin.register(SensorReading)
class SensorReadingAdmin(admin.ModelAdmin):
    list_display = (
        "timestamp",
        "temperature",
        "humidity",
        "gas_value",
    )
    readonly_fields = [
        "id",
        "timestamp",
    ]
