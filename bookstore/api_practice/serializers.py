
# serializers.py
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['created_at', 'status', 'id', 'user']
        read_only_fields = ['id', 'created_at']