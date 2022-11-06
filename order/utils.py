import requests
from shoe.models import Shoe
from django.db.models import Sum

def generate_random_float():
    url="http://www.randomnumberapi.com/api/v1.0/random?min=0&max=1000"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]/100
    else:
        raise Exception("API call failed")

def validate_lines(lines):
    shoe_requests = lines.values('shoe').annotate(total_quantity=Sum('quantity'))
    for shoe_request in shoe_requests:
        stock = Shoe.objects.get(id=shoe_request["shoe"]).stock
        if stock < shoe_request["total_quantity"]:
            raise Exception("Insufficient stock")

def reduce_stock(lines):
    shoe_requests = lines.values('shoe').annotate(total_quantity=Sum('quantity'))
    for shoe_request in shoe_requests:
        shoe = Shoe.objects.get(id=shoe_request["shoe"])
        shoe.stock = shoe.stock - shoe_request["total_quantity"]
        shoe.save()
