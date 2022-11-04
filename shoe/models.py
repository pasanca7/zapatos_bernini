from django.db import models

currencies = [
        ('€', 'EURO (€)'),
    ]

class Shoe(models.Model):
    name = models.CharField(max_length=255)
    currency = models.CharField(max_length=5, choices=currencies, default="€")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name + '-' + self.size