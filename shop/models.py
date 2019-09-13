from django.db import models
from django.conf import settings

from products.models import Product
from cart.models import CartItem


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ManyToManyField(CartItem)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + ':' + str(self.pk)

