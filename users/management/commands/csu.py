from django.core.management import BaseCommand
from users.models import User
import os


PASSWORD = '12345'

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='miklefil94@yahoo.com',
            first_name='Admin',
            last_name='SuperUser',
            is_staff=True,
            is_superuser=True
        )

        user.set_password(PASSWORD)
        user.save()