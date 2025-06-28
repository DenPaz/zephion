from allauth.account.forms import AddEmailForm as AllauthAddEmailForm
from allauth.account.forms import ChangePasswordForm as AllauthChangePasswordForm
from allauth.account.forms import LoginForm as AllauthLoginForm
from allauth.account.forms import ReauthenticateForm as AllauthReauthenticateForm
from allauth.account.forms import ResetPasswordForm as AllauthResetPasswordForm
from allauth.account.forms import ResetPasswordKeyForm as AllauthResetPasswordKeyForm
from allauth.account.forms import SetPasswordForm as AllauthSetPasswordForm
from allauth.account.forms import SignupForm as AllauthSignupForm
from allauth.account.forms import UserTokenForm as AllauthUserTokenForm
from django.utils.translation import gettext_lazy as _


class LoginForm(AllauthLoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].label = _("E-mail")
        self.fields["login"].widget.attrs.update(
            {
                "class": "form-control form-control-lg form-control-solid",
                "autofocus": True,
                "type": "email",
                "placeholder": _("Insira seu e-mail"),
            },
        )
        self.fields["password"].label = _("Senha")
        self.fields["password"].widget.attrs.update(
            {
                "class": "form-control form-control-lg form-control-solid",
                "type": "password",
                "placeholder": _("Insira sua senha"),
            },
        )
        self.fields["remember"].label = _("Lembrar-me")
        self.fields["remember"].widget.attrs.update(
            {
                "class": "form-check-input",
                "type": "checkbox",
            },
        )


class ResetPasswordForm(AllauthResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = _("E-mail")
        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control form-control-lg form-control-solid",
                "autofocus": True,
                "type": "email",
                "placeholder": _("Insira seu e-mail"),
            },
        )


class ResetPasswordKeyForm(AllauthResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].label = _("Nova senha")
        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-control form-control-lg form-control-solid",
                "type": "password",
                "placeholder": _("Insira sua nova senha"),
            },
        )
        self.fields["password2"].label = _("Confirmar senha")
        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control form-control-lg form-control-solid",
                "type": "password",
                "placeholder": _("Confirme sua nova senha"),
            },
        )


class AddEmailForm(AllauthAddEmailForm):
    pass


class ChangePasswordForm(AllauthChangePasswordForm):
    pass


class ReauthenticateForm(AllauthReauthenticateForm):
    pass


class SetPasswordForm(AllauthSetPasswordForm):
    pass


class SignupForm(AllauthSignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = _("E-mail")
        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control form-control-lg form-control-solid",
                "autofocus": True,
                "type": "email",
                "placeholder": _("Insira seu e-mail"),
            },
        )
        self.fields["first_name"].label = _("Nome")
        self.fields["first_name"].widget.attrs.update(
            {
                "class": "form-control form-control-lg form-control-solid",
                "type": "text",
                "placeholder": _("Insira seu nome"),
            },
        )
        self.fields["last_name"].label = _("Sobrenome")
        self.fields["last_name"].widget.attrs.update(
            {
                "class": "form-control form-control-lg form-control-solid",
                "type": "text",
                "placeholder": _("Insira seu sobrenome"),
            },
        )
        self.fields["password1"].label = _("Senha")
        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-control form-control-lg form-control-solid",
                "type": "password",
                "placeholder": _("Insira sua senha"),
            },
        )
        self.fields["password2"].label = _("Confirmar senha")
        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control form-control-lg form-control-solid",
                "type": "password",
                "placeholder": _("Confirme sua senha"),
            },
        )


class UserTokenForm(AllauthUserTokenForm):
    pass
