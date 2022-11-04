from rest_framework.viewsets import ModelViewSet
from shoe.models import Shoe
from shoe.api.serializers import ShoeSerializer

class ShoeApiViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    queryset = Shoe.objects.all()