from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _


class AccountAdapter(DefaultAccountAdapter):
    error_messages = {
        **DefaultAccountAdapter.error_messages,
        "account_inactive": _(
            "Esta conta está inativa. Entre em contato com o administrador.",
        ),
        "username_password_mismatch": _(
            "O usuário e/ou senha especificados estão incorretos.",
        ),
        "too_many_login_attempts": _(
            "Muitas tentativas de login. Tente novamente mais tarde.",
        ),
        "unverified_primary_email": _(
            "O endereço de e-mail principal não foi verificado.",
        ),
    }

    def is_open_for_signup(self, request: HttpRequest) -> bool:
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
