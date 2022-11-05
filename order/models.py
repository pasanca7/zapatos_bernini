from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator
from shoe.models import Shoe

currencies = [
        ('€', 'EURO (€)'),
    ]

class Order(models.Model):
    created = models.DateTimeField(default=now, editable=False)
    status = models.CharField(max_length=255, default='PENDING')
    currency = models.CharField(max_length=5, choices=currencies, default="€")
    shipping_costs = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.total_amount) + " " + str(self.currency) +"(" + str(self.created) + ")"

class OrderLine(models.Model):
    shoe = models.ForeignKey(
        Shoe,
        related_name="order_lines",
        on_delete=models.SET_NULL,
        null=True,
    )
    order = models.ForeignKey(
        Order,
        related_name="order_lines",
        on_delete=models.CASCADE,
        null=True,
    )
    shoe_name = models.CharField(max_length=255)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=5, choices=currencies, default="€")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return str(self.shoe_name) +"(" + str(self.quantity) + ")"
