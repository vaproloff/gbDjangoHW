from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = "Get client"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Get client by ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{client}')
