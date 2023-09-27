from django.core.management.base import BaseCommand
from shop_app.models import Product


class Command(BaseCommand):
    help = "Get product"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Get product by ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        self.stdout.write(f'{product}')
