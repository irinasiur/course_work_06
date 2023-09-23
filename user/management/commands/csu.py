from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='drozdovairina10@gmail.com',
            first_name='Admin',
            last_name='Home',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('q1')
        user.save()
