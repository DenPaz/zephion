from django.core.management.base import BaseCommand

from apps.users.models import User
from apps.users.models import UserProfile

data = [
    {
        "first_name": "Dennis",
        "last_name": "Paz",
        "email": "dppazlopez@gmail.com",
        "is_superuser": True,
        "is_staff": True,
    },
]
default_password = "2305"  # noqa: S105


class Command(BaseCommand):
    help = "Add or update users in the database."

    def handle(self, *args, **kwargs):
        for entry in data:
            email = entry["email"]

            user_fields = {
                k: entry[k]
                for k in (
                    "first_name",
                    "last_name",
                    "email",
                    "is_superuser",
                    "is_staff",
                )
            }
            profile_fields = {k: v for k, v in entry.items() if k not in user_fields}

            user, created_user = User.objects.update_or_create(
                email=email,
                defaults=user_fields,
            )
            if created_user:
                user.set_password(default_password)
                user.save()
            msg = (
                f"{'Created' if created_user else 'Updated'} "
                f"{User.__name__} with email: {user.email}"
            )
            self.stdout.write(
                self.style.SUCCESS(msg) if created_user else self.style.WARNING(msg),
            )

            profile, created_profile = UserProfile.objects.update_or_create(
                user=user,
                defaults=profile_fields,
            )
            msg = (
                f"{'Created' if created_profile else 'Updated'} "
                f"{UserProfile.__name__}: {profile}"
            )
            self.stdout.write(
                self.style.SUCCESS(msg) if created_profile else self.style.WARNING(msg),
            )
