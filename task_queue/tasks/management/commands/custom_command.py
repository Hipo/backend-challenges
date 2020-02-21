from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        pass
