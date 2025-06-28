from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UppercaseValidator:
    def validate(self, password, user=None):
        if not any(char.isupper() for char in password):
            msg = _("A senha deve conter pelo menos uma letra maiúscula.")
            raise ValidationError(msg, code="password_no_upper")

    def get_help_text(self):
        return _("A senha deve conter pelo menos uma letra maiúscula.")


class LowercaseValidator:
    def validate(self, password, user=None):
        if not any(char.islower() for char in password):
            msg = _("A senha deve conter pelo menos uma letra minúscula.")
            raise ValidationError(msg, code="password_no_lower")

    def get_help_text(self):
        return _("A senha deve conter pelo menos uma letra minúscula.")
