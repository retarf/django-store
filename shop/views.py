from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse

from .models import Cart, Order, OrderItem
from products.models import Product

#class CartView(generic.DetailView):
#    template_name = 'shop/cart.html'
#    model = Cart

def show_user(request):
    user = request.user
    response = "<h1>{0}</h1>".format(user)
    return HttpResponse(response)

