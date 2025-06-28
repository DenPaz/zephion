from allauth.account.decorators import secure_admin_login
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms_admin import UserAdminChangeForm
from .forms_admin import UserAdminCreationForm
from .models import User
from .models import UserProfile

if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
    admin.autodiscover()
    admin.site.login = secure_admin_login(admin.site.login)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    min_num = 1
    max_num = 1
    verbose_name = _("Informações adicionais")
    can_delete = False
    fk_name = "user"


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    inlines = [UserProfileInline]
    fieldsets = (
        (
            _("Informações da conta"),
            {
                "fields": (
                    "id",
                    "first_name",
                    "last_name",
                    "email",
                    "password",
                    "is_active",
                    "last_login",
                    "date_joined",
                ),
            },
        ),
        (
            _("Permissões"),
            {
                "classes": ("collapse",),
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            _("Informações da conta"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                ),
            },
        ),
    )
    list_display = [
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    list_filter = [
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    filter_horizontal = [
        "groups",
        "user_permissions",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "email",
    ]
    ordering = [
        "first_name",
        "last_name",
    ]
    readonly_fields = [
        "id",
        "last_login",
        "date_joined",
    ]
    list_per_page = 10
