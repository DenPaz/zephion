from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def add_class_if_url(context, *url_names, class_name="active"):
    request = context.get("request")
    if not request:
        return ""
    resolver_match = getattr(request, "resolver_match", None)
    if not resolver_match:
        return ""
    if resolver_match.view_name in url_names:
        return class_name
    return ""


@register.filter
def get_filename(file):
    if not file:
        return ""
    return file.split("/")[-1] if "/" in file else file
