from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("apps.dashboard.urls", namespace="dashboard")),
    path("users/", include("apps.users.urls", namespace="users")),
    path("sensors/", include("apps.sensors.urls", namespace="sensors")),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

urlpatterns += [
    path("api/", include("config.api_routers")),
    path("api/auth-token/", obtain_auth_token, name="obtain_auth_token"),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

if settings.DEBUG:
    urlpatterns += [
        path(
            route="400/",
            view=default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            route="403/",
            view=default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            route="404/",
            view=default_views.page_not_found,
            kwargs={"exception": Exception("Page Not Found")},
        ),
        path(
            route="500/",
            view=default_views.server_error,
        ),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
            *urlpatterns,
        ]
