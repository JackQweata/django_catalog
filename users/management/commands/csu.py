from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@sky.pro',
            first_name='Admin',
            phone='88005545',
            country='Россия',
            is_verified=True,
            last_name='SkyPro',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123')
        user.save()