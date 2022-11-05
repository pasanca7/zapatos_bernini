from .models import Shoe
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShoeSerializer
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

@api_view(['GET'])
@cache_page(60)
@vary_on_headers('Authorization')
def shoeList(request):
	shoes = Shoe.objects.all().order_by('-id')
	serializer = ShoeSerializer(shoes, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@cache_page(60)
@vary_on_headers('Authorization')
def shoeDetail(request, pk):
	shoe = Shoe.objects.filter(id=pk).first()
	if shoe:
		serializer = ShoeSerializer(shoe, many=False)
		return Response(serializer.data, status=status.HTTP_200_OK)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def shoeCreate(request):
	serializer = ShoeSerializer(data=request.data)
	if request.user.is_superuser:
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return  Response(status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
def shoeUpdate(request, pk):
	shoe = Shoe.objects.filter(id=pk).first()
	if request.user.is_superuser:
		if shoe:
			serializer = ShoeSerializer(instance=shoe, data=request.data)

			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			else:
				return Response(status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)
	else:
		return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['DELETE'])
def shoeDelete(request, pk):
	shoe = Shoe.objects.filter(id=pk).first()
	if request.user.is_superuser:
		if shoe:
			shoe.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)
	else:
		return Response(status=status.HTTP_401_UNAUTHORIZED)

