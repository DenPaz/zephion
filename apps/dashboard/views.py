import json

from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from apps.core.viewmixins import HTMXTemplateMixin
from apps.sensors.models import SensorReading


class IndexView(HTMXTemplateMixin, TemplateView):
    template_name = "dashboard/index.html"
    htmx_template_name = "dashboard/partials/charts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        readings = SensorReading.objects.order_by("-timestamp")[:50][::-1]
        context.update(
            {
                "page_title": "Dashboard",
                "page_description": _("Bem-vindo ao Zephion"),
                "labels": json.dumps(
                    [
                        timezone.localtime(r.timestamp).strftime("%Y-%m-%d %H:%M:%S")
                        for r in readings
                    ],
                    cls=DjangoJSONEncoder,
                ),
                "temp_data": json.dumps(
                    [r.temperature for r in readings],
                    cls=DjangoJSONEncoder,
                ),
                "hum_data": json.dumps(
                    [r.humidity for r in readings],
                    cls=DjangoJSONEncoder,
                ),
                "gas_data": json.dumps(
                    [r.gas_value for r in readings],
                    cls=DjangoJSONEncoder,
                ),
            },
        )
        return context
