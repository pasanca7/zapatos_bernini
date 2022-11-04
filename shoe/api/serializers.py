from rest_framework.serializers import ModelSerializer
from shoe.models import Shoe

class ShoeSerializer(ModelSerializer):
    class Meta:
        model = Shoe
        fields = ["id", "name", "price", "size", "currency", "stock"]