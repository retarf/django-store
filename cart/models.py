from django.db import models
from django.conf import settings

from products.models import Product

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    @property
    def value(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ManyToManyField(CartItem)

    def __str__(self):
        return self.user

