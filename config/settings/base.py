# ruff: noqa: E501
from pathlib import Path

import environ
from django.contrib.messages import constants as messages
from django.utils.translation import gettext_lazy as _

# -----------------------------------------------------------------------------
# PATHS
# -----------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# -----------------------------------------------------------------------------
# ENVIRONMENT
# -----------------------------------------------------------------------------
env = environ.Env()
READ_DOT_ENV_FILE = env.bool(
    "DJANGO_READ_DOT_ENV_FILE",
    default=False,
)
if READ_DOT_ENV_FILE:
    env.read_env(str(BASE_DIR / ".env"))

# -----------------------------------------------------------------------------
# GENERAL
# -----------------------------------------------------------------------------
DEBUG = env.bool(
    "DJANGO_DEBUG",
    default=False,
)
TIME_ZONE = "America/Sao_Paulo"
LANGUAGE_CODE = "pt-BR"
LANGUAGES = [
    ("en", _("Inglês")),
    ("pt-br", _("Português")),
]
SITE_ID = 1
USE_I18N = True
USE_TZ = True
LOCALE_PATHS = [str(BASE_DIR / "locale")]

# -----------------------------------------------------------------------------
# DATABASES
# -----------------------------------------------------------------------------
DATABASES = {
    "default": env.db(
        "DATABASE_URL",
        default="sqlite:///db.sqlite3",
    ),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -----------------------------------------------------------------------------
# URLS
# -----------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# -----------------------------------------------------------------------------
# APPS
# -----------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    "allauth.mfa",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "drf_spectacular",
    "braces",
    "django_htmx",
    "django_cotton",
    "widget_tweaks",
    "django_filters",
]
LOCAL_APPS = [
    "apps.core.config.CoreConfig",
    "apps.dashboard.config.DashboardConfig",
    "apps.users.config.UsersConfig",
    "apps.sensors.config.SensorsConfig",
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# -----------------------------------------------------------------------------
# MIGRATIONS
# -----------------------------------------------------------------------------
MIGRATION_MODULES = {}

# -----------------------------------------------------------------------------
# AUTHENTICATION
# -----------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "dashboard:index"
LOGOUT_REDIRECT_URL = "account_login"
LOGIN_URL = "account_login"

# -----------------------------------------------------------------------------
# PASSWORDS
# -----------------------------------------------------------------------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
    {"NAME": "apps.users.password_validation.UppercaseValidator"},
    {"NAME": "apps.users.password_validation.LowercaseValidator"},
]

# -----------------------------------------------------------------------------
# MIDDLEWARE
# -----------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.LoginRequiredMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]

# -----------------------------------------------------------------------------
# STATIC
# -----------------------------------------------------------------------------
STATIC_ROOT = str(BASE_DIR / "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(BASE_DIR / "static")]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# -----------------------------------------------------------------------------
# MEDIA
# -----------------------------------------------------------------------------
MEDIA_ROOT = str(BASE_DIR / "media")
MEDIA_URL = "/media/"

# -----------------------------------------------------------------------------
# TEMPLATES
# -----------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "apps.users.context_processors.allauth_settings",
            ],
        },
    },
]
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# -----------------------------------------------------------------------------
# FIXTURES
# -----------------------------------------------------------------------------
FIXTURE_DIRS = (str(BASE_DIR / "fixtures"),)

# -----------------------------------------------------------------------------
# SECURITY
# -----------------------------------------------------------------------------
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = "DENY"

# -----------------------------------------------------------------------------
# EMAIL
# -----------------------------------------------------------------------------
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
EMAIL_TIMEOUT = 5

# -----------------------------------------------------------------------------
# ADMIN
# -----------------------------------------------------------------------------
ADMIN_URL = "admin/"
ADMINS = [
    ("""Dennis Paz""", "dppazlopez@gmail.com"),
]
MANAGERS = ADMINS
DJANGO_ADMIN_FORCE_ALLAUTH = env.bool(
    "DJANGO_ADMIN_FORCE_ALLAUTH",
    default=True,
)

# -----------------------------------------------------------------------------
# MESSAGES
# -----------------------------------------------------------------------------
MESSAGE_TAGS = {
    messages.ERROR: "danger",
}

# -----------------------------------------------------------------------------
# redis
# -----------------------------------------------------------------------------
REDIS_URL = env(
    "REDIS_URL",
    default="redis://localhost:6379/0",
)
REDIS_SSL = REDIS_URL.startswith("rediss://")

# -----------------------------------------------------------------------------
# django-allauth
# -----------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool(
    "DJANGO_ACCOUNT_ALLOW_REGISTRATION",
    default=True,
)
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = [
    "email*",
    "password1*",
    "password2*",
]
ACCOUNT_SIGNUP_FORM_CLASS = "apps.users.forms.SignupForm"
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_ADAPTER = "apps.users.adapters.AccountAdapter"
ACCOUNT_FORMS = {
    "add_email": "apps.users.forms_allauth.AddEmailForm",
    "change_password": "apps.users.forms_allauth.ChangePasswordForm",
    "login": "apps.users.forms_allauth.LoginForm",
    "reauthenticate": "apps.users.forms_allauth.ReauthenticateForm",
    "reset_password": "apps.users.forms_allauth.ResetPasswordForm",
    "reset_password_from_key": "apps.users.forms_allauth.ResetPasswordKeyForm",
    "set_password": "apps.users.forms_allauth.SetPasswordForm",
    "signup": "apps.users.forms_allauth.SignupForm",
    "user_token": "apps.users.forms_allauth.UserTokenForm",
}
ACCOUNT_CHANGE_EMAIL = True
ACCOUNT_EMAIL_UNKNOWN_ACCOUNTS = False

# -----------------------------------------------------------------------------
# django-rest-framework
# -----------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        # "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.AllowAny",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# -----------------------------------------------------------------------------
# django-cors-headers
# -----------------------------------------------------------------------------
CORS_URLS_REGEX = r"^/api/.*$"
SPECTACULAR_SETTINGS = {
    "TITLE": "Zephion API",
    "DESCRIPTION": "Documentation of API endpoints of Zephion",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
    "SCHEMA_PATH_PREFIX": "/api/",
}

# -----------------------------------------------------------------------------
# django-cotton
# -----------------------------------------------------------------------------
COTTON_DIR = "components"
