from rest_framework import serializers
from shoe.serializers import ShoeSerializer
from shoe.models import Shoe
from order.models import OrderLine, Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["created", "status", "currency", "shipping_costs", "total_amount"]


class OrderLineSerializer(serializers.ModelSerializer):
    shoe = serializers.PrimaryKeyRelatedField(allow_null=False, many=False,queryset=Shoe.objects.all())
    order = serializers.PrimaryKeyRelatedField(allow_null=True, many=False, queryset=Order.objects.all())
    total_amount = serializers.SerializerMethodField('get_total_amount')
    currency = serializers.SerializerMethodField('get_currency')
    shoe_name = serializers.SerializerMethodField('get_shoe_name')
    
    class Meta:
        model = OrderLine
        fields = ["id", "order", "shoe", "shoe_name", "quantity", "total_amount", "currency"]
    
    def get_shoe_name(self, obj):
        return obj.shoe.name

    def get_currency(self, obj):
        return obj.shoe.currency

    def get_total_amount(self, obj):
        return obj.quantity * obj.shoe.price
    
    