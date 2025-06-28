from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DevicesConfig(AppConfig):
    name = "apps.devices"
    verbose_name = _("Dispositivos")
