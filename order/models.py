from itertools import product
from django.db import models
from customer.models import Customer
from product.models import Product



class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.quantity)