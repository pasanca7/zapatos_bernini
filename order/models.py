from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator
from shoe.models import Shoe

currencies = [
        ('€', 'EURO (€)'),
    ]

class OrderLine(models.Model):
    order = models.ForeignKey(
        "Order",
        related_name="lines",
        editable=False,
        on_delete=models.CASCADE,
    ),
    Shoe = models.ForeignKey(
        Shoe,
        related_name="orderLines",
        on_delete=models.SET_NULL,
        null=True
    )
    shoe_name = models.CharField(max_length=255)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=5, choices=currencies, default="€")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.shoe_name +"(" + self.quantity + ")"

class Order(models.Model):
    created = models.DateTimeField(default=now, editable=False)
    status = models.CharField(max_length=255, default='PENDING')
    currency = models.CharField(max_length=5, choices=currencies, default="€")
    shipping_costs = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.total_amount + " "+ self.currency +"(" + self.created + ")"
