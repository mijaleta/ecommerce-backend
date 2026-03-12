# serializers.py
from rest_framework import serializers
from .models import Order, OrderItem, ShippingInfo

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class ShippingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingInfo
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    shipping = ShippingInfoSerializer(read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'