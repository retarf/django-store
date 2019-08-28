from django.shortcuts import render
from django.views import generic

from .models import Product

class IndexView(generic.ListView):
    template_name = 'products/index.html'
    module = Product

    def get_queryset(self):
        return Product.objects.all()
