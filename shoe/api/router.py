from rest_framework.routers import DefaultRouter
from shoe.api.views import ShoeApiViewSet

router_shoe = DefaultRouter()

router_shoe.register(prefix='shoe', basename='shoe', viewset=ShoeApiViewSet)