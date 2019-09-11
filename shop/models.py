from django.db import models
from django.conf import settings


from products.models import Product

# Create your models here.
class OrderItem(models.Model):
    #product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    @property
    def value(self):
        self.product.price * self.quantity

    def __str__(self):
        return self.product.name

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ManyToManyField(OrderItem)

    def __str__(self):
        return self.user

class Order(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    # FIXME: change ordered to sent

    def __str__(self):
        return self.user.username + ':' + str(self.pk)

