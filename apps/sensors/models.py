from django.db import models
from django.utils.translation import gettext_lazy as _


class SensorReading(models.Model):
    id = models.BigAutoField(
        verbose_name=_("ID"),
        primary_key=True,
    )
    timestamp = models.DateTimeField(
        verbose_name=_("Timestamp"),
        auto_now_add=True,
    )
    temperature = models.FloatField(
        verbose_name=_("Temperatura"),
    )
    humidity = models.FloatField(
        verbose_name=_("Humidade"),
    )
    gas_value = models.IntegerField(
        verbose_name=_("Valor do gás"),
    )

    class Meta:
        verbose_name = _("Leitura dos sensores")
        verbose_name_plural = _("Leituras dos sensores")
        ordering = ["-timestamp"]

    def __str__(self):
        return (
            f"{self.timestamp}: {self.temperature}°C | "
            f"{self.humidity}% | {self.gas_value}ppm"
        )
