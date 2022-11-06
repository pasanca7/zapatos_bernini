from order.models import OrderLine, Order
from shoe.models import Shoe
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderLineSerializer, OrderSerializer
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from order import utils

@api_view(['GET'])
@cache_page(60)
@vary_on_headers('Authorization')
def lineList(request):
	lines = OrderLine.objects.all().order_by('-id')
	serializer = OrderLineSerializer(lines, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@cache_page(60)
@vary_on_headers('Authorization')
def lineDetail(request, pk):
    line = OrderLine.objects.filter(id=pk).first()
    if line:
        serializer = OrderLineSerializer(line, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def lineCreate(request):
    try :
        shoe = Shoe.objects.filter(id=request.data['shoe']).first()
        request.data["shoe_name"]=shoe.name
        request.data["currency"]=shoe.currency
        request.data["total_amount"]=request.data["quantity"] * shoe.price
        serializer = OrderLineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def lineUpdate(request, pk):
    line = OrderLine.objects.filter(id=pk).first()
    if line:
        request.data["shoe_name"]=line.shoe.name
        serializer = OrderLineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def lineDelete(request, pk):
    line = OrderLine.objects.filter(id=pk).first()
    if line:
        line.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@cache_page(60)
@vary_on_headers('Authorization')
def orderList(request):
    if request.user.is_superuser:
        orders = Order.objects.all().order_by('-id')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@cache_page(60)
@vary_on_headers('Authorization')
def orderDetail(request, pk):
    order = Order.objects.filter(id=pk).first()
    if order:
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def orderCreate(request):
    line_ids = request.data.get('lines')
    try:
        lines = OrderLine.objects.filter(id__in=line_ids)
        utils.validate_lines(lines)
        random_float = utils.generate_random_float()
        request.data["user"] = request.user.id
        request.data["shipping_costs"] = random_float
        request.data["currency"] = lines.first().currency
        request.data["total_amount"] = random_float + float(lines.aggregate(Sum('total_amount'))["total_amount__sum"])
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            utils.reduce_stock(lines)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

