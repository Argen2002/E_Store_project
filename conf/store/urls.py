from django.urls import path
from .views import ProductListAPIView, OrderListCreateView

urlpatterns = [
    path('/products/', ProductListAPIView.as_view(), name='product-list'),
    path('/orders/', OrderListCreateView.as_view(), name='order-list-create'),
]
