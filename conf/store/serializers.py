from rest_framework import serializers
from .models import books

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = '__all__'


from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
