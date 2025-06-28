from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdminChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        field_classes = {
            "email": forms.EmailField,
        }


class UserAdminCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
        )
        error_messages = {
            "email": {"unique": _("Esse e-mail já está em uso.")},
        }

    def save(self, *, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get("password"):
            user.set_password(self.cleaned_data["password"])
        else:
            user.set_unusable_password()
        if commit:
            user.save()
        return user
