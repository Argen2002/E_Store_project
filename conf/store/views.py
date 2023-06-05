from rest_framework import generics
from .models import books, Order
from .serializers import ProductSerializer, OrderSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = books.objects.all()
    serializer_class = ProductSerializer



class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)