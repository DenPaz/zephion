# ruff: noqa: E501
from .base import *  # noqa: F403
from .base import INSTALLED_APPS
from .base import MIDDLEWARE
from .base import env

# -----------------------------------------------------------------------------
# GENERAL
# -----------------------------------------------------------------------------
DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="1ns3cure-s3cr3t-k3y",
)
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",  # noqa: S104
    "127.0.0.1",
    "192.168.1.6",
    "7fb257d5c410-1468329044895344350.ngrok-free.app",
]
CSRF_TRUSTED_ORIGINS = [
    "https://7fb257d5c410-1468329044895344350.ngrok-free.app",
]

# -----------------------------------------------------------------------------
# CACHES
# -----------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    },
}

# -----------------------------------------------------------------------------
# EMAIL
# -----------------------------------------------------------------------------
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)

# -----------------------------------------------------------------------------
# LOGGING
# -----------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# -----------------------------------------------------------------------------
# whitenoise
# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    *INSTALLED_APPS,
]

# -----------------------------------------------------------------------------
# django-debug-toolbar
# -----------------------------------------------------------------------------
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": [
        "debug_toolbar.panels.redirects.RedirectsPanel",
        "debug_toolbar.panels.profiling.ProfilingPanel",
    ],
    "SHOW_TEMPLATE_CONTEXT": True,
}
INTERNAL_IPS = [
    "127.0.0.1",
    "10.0.2.2",
]

# -----------------------------------------------------------------------------
# django-extensions
# -----------------------------------------------------------------------------
INSTALLED_APPS += ["django_extensions"]
