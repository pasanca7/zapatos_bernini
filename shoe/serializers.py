from rest_framework.serializers import ModelSerializer
from .models import Shoe

class ShoeSerializer(ModelSerializer):
    class Meta:
        model = Shoe
        fields = '__all__'