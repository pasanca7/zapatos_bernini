from django.contrib import admin
from order.models import Order, OrderLine

@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "shoe",
        "shoe_name",
        "quantity",
        "currency",
        "total_amount"
    ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "created",
        "status",
        "currency",
        "shipping_costs",
        "total_amount"
    ]
