from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Cart, CartItem
from products.models import Product
from shop.models import Order

@login_required
def index(request):

    user = User.objects.get(username=request.user)
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cart = Cart()
        cart.user = user
        cart.save()

    content = {'cart': cart}
    template = 'cart/cart.html'

    return render(request, template, content)

def add(request, product_id):

    user = User.objects.get(username=request.user)
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cart = Cart()
        cart.user = user
        cart.save()

    product = Product.objects.get(pk=product_id)

    item = CartItem()
    item.product = product
    item.quantity = 1
    item.save()

    cart.item.add(item)

    return redirect('products:index')

@login_required
def send(request):
     
    user = User.objects.get(username=request.user)
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cart = Cart()
        cart.user = user
        cart.save()
        
    order = Order()
    order.user = user
    order.save()
    order.item.set(cart.item.all())
    order.save()

    cart.delete()

    return redirect('products:index')
