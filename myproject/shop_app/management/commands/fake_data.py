import random

from django.core.management.base import BaseCommand
from shop_app.models import Client, Product, Order


class Command(BaseCommand):
    help = "Create fake Clients, Products, Orders"

    def add_arguments(self, parser):
        parser.add_argument('clients_qty', type=int, help='Fake clients count')
        parser.add_argument('products_qty', type=int, help='Fake products count')
        parser.add_argument('orders_qty', type=int, help='Fake orders count')

    def handle(self, *args, **kwargs):
        clients_qty = kwargs.get('clients_qty')
        products_qty = kwargs.get('products_qty')
        orders_qty = kwargs.get('orders_qty')

        products = []
        clients = []

        for i in range(1, products_qty + 1):
            product = Product(name=f'product_{i}',
                              price=random.uniform(1.0, 100.0),
                              quantity=random.randint(0, 100))
            product.save()
            products.append(product)

        for i in range(1, clients_qty + 1):
            client = Client(name=f'Name_{i}',
                            email=f'user_{i}@mail.ru',
                            phone=f'+79{random.randint(100000000, 999999999)}')
            client.save()
            clients.append(client)

        for i in range(1, orders_qty + 1):
            order = Order(client=random.choice(clients),
                          total_amount=random.uniform(10.0, 300.0))
            order.save()
            for _ in range(random.randint(1, 3)):
                product = random.choice(products)
                order.products.add(product)
                order.save()
