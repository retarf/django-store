from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, default='Product')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, default=0.0, decimal_places=2)

    def __str__(self):
        return self.name
