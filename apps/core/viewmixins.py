from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django_htmx.http import HttpResponseClientRedirect


class HTMXTemplateMixin:
    htmx_template_name = None

    def dispatch(self, request, *args, **kwargs):
        if self.htmx_template_name is None:
            msg = f"'{self.__class__.__name__}' must define 'htmx_template_name'."
            raise ImproperlyConfigured(msg)
        return super().dispatch(request, *args, **kwargs)

    def get_template_names(self):
        if self.request.htmx and self.htmx_template_name:
            return [self.htmx_template_name]
        return super().get_template_names()


class HtmxRedirectMixin:
    def get_htmx_redirect_url(self):
        return self.get_success_url()

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.htmx and isinstance(response, HttpResponseRedirect):
            return HttpResponseClientRedirect(self.get_htmx_redirect_url())
        return response

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if self.request.htmx and isinstance(response, HttpResponseRedirect):
            return HttpResponseClientRedirect(response.url)
        return response

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        if self.request.htmx and isinstance(response, HttpResponseRedirect):
            return HttpResponseClientRedirect(response.url)
        return response
