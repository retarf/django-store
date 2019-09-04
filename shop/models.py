from django.db import models
from django.conf import settings


from products.models import Product

# Create your models here.

class Cart(models.Model):
    # TODO: Implement user authorization and session
    user = models.CharField(blank=True, max_length=50)
    products = models.ManyToManyField(Product)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.user

class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

class Order(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ManyToManyField(OrderItem)

