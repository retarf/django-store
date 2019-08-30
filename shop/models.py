from django.db import models

from products.models import Product

# Create your models here.

class Cart(models.Model):
    # TODO: Implement user authorization and session
    user = models.CharField(blank=True, max_length=50)
    products = models.ManyToManyField(Product)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.user



