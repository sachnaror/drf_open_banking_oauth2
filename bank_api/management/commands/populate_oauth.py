import random
from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from oauth2_provider.models import AccessToken, Application, RefreshToken


class Command(BaseCommand):
    help = "Populate database with test users, OAuth2 applications, and tokens"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating test users...")

        users = []
        roles = ["customer", "merchant", "admin", "auditor", "developer"]

        for i in range(1, 11):  # Creating 10 users
            user, created = User.objects.get_or_create(
                username=f"user{i}",
                defaults={"email": f"user{i}@example.com", "is_staff": False}
            )
            user.set_password("password123")  # Set a common password
            user.save()
            users.append((user, random.choice(roles)))

        self.stdout.write("✅ 10 test users created.")

        self.stdout.write("Creating OAuth2 applications...")

        app1 = Application.objects.create(
            name="Banking App",
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_AUTHORIZATION_CODE,
            user=users[0][0],  # Assign the first user as owner
        )

        app2 = Application.objects.create(
            name="Fintech API",
            client_type=Application.CLIENT_PUBLIC,
            authorization_grant_type=Application.GRANT_PASSWORD,
            user=users[1][0],  # Assign the second user as owner
        )

        self.stdout.write(f"✅ Created OAuth Applications:\n  - {app1.name} (Client ID: {app1.client_id})\n  - {app2.name} (Client ID: {app2.client_id})")

        self.stdout.write("Generating OAuth2 Tokens...")

        for user, role in users:
            access_token = AccessToken.objects.create(
                user=user,
                application=app1 if random.choice([True, False]) else app2,
                token=f"access_{user.username}",
                expires=now() + timedelta(hours=1),
                scope="read write" if role in ["admin", "developer"] else "read",
            )

            RefreshToken.objects.create(
                user=user,
                application=access_token.application,
                token=f"refresh_{user.username}",
                access_token=access_token
            )

            self.stdout.write(f"✅ User {user.username} ({role}) - Access Token: {access_token.token}")

        self.stdout.write("🎉 Test data inserted successfully!")
