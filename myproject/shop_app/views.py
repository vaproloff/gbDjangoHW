import logging
from django.http import HttpResponse
from shop_app.models import Client, Product, Order

logger = logging.getLogger(__name__)


def get_clients(request):
    logger.info(f'{request} request received!')
    client_id = request.GET.get('id')
    if client_id:
        response = Client.objects.filter(pk=client_id)
    else:
        response = Client.objects.all()
    return HttpResponse(response)


def get_orders_by_client(request):
    logger.info(f'{request} request received!')
    client_id = request.GET.get('client_id')
    orders = Order.objects.filter(client=client_id).all()
    return HttpResponse(orders)


def get_products(request):
    logger.info(f'{request} request received!')
    product_id = request.GET.get('id')
    if product_id:
        response = Product.objects.filter(pk=product_id)
    else:
        response = Product.objects.all()
    return HttpResponse(response)
