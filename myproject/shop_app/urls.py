from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:product_id>/', views.ProductView.as_view(), name='product_by_id'),
    path('orders/<int:order_id>/', views.OrderView.as_view(), name='order_by_id'),
    path('clients/<int:client_id>/orders/', views.ClientOrdersView.as_view(), name='client_orders'),
    path('clients/<int:client_id>/products/<int:period>/', views.ClientProductsView.as_view(), name='client_products'),
]
