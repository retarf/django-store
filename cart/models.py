from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from products.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    @property
    def value(self):
        return self.product.price * self.quantity

    def __str__(self):
        #return product.name
        return 'test'

