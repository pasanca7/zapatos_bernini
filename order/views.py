from .models import OrderLine, Order
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderLineSerializer

@api_view(['GET'])
def lineList(request):
	lines = OrderLine.objects.all().order_by('-id')
	serializer = OrderLineSerializer(lines, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def lineDetail(request, pk):
    line = OrderLine.objects.filter(id=pk).first()
    if line:
        serializer = OrderLineSerializer(line, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def lineCreate(request):
    serializer = OrderLineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def lineUpdate(request, pk):
    line = OrderLine.objects.filter(id=pk).first()
    if line:
        serializer = OrderLineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
