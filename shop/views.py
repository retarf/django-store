from django.shortcuts import render
from django.views import generic

from .models import Cart

class CartView(generic.DetailView):
    template_name = 'shop/cart.html'
    model = Cart
