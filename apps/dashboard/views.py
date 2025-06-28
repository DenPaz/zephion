from django.utils.translation import gettext as _
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "dashboard/index.html"
    extra_context = {
        "page_title": "Dashboard",
        "page_description": _("Bem-vindo ao Zephion"),
    }
