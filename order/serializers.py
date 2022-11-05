from rest_framework import serializers
from shoe.serializers import ShoeSerializer
from shoe.models import Shoe
from django.contrib.auth.models import User
from order.models import OrderLine, Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderLineSerializer(serializers.ModelSerializer):
    shoe = serializers.PrimaryKeyRelatedField(allow_null=False, many=False,queryset=Shoe.objects.all())
    order = serializers.PrimaryKeyRelatedField(allow_null=True, many=False, queryset=Order.objects.all())
    user = serializers.PrimaryKeyRelatedField(allow_null=True, many=False, queryset=User.objects.all())
    
    class Meta:
        model = OrderLine
        fields = "__all__"
    