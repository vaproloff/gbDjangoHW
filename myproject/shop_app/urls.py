from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.get_clients, name='get_client_by_id'),
    path('products/', views.get_products, name='get_product_by_id'),
    path('orders/', views.get_orders_by_client, name='get_product_by_id'),
]
