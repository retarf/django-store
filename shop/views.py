from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError

from .models import Cart, Order, OrderItem
from products.models import Product

#class CartView(generic.DetailView):
#    template_name = 'shop/cart.html'
#    model = Cart

def show_user(request):
    user = request.user
    response = "<h1>{0}</h1>".format(user)
    return HttpResponse(response)

@login_required
def cart(request):

    user = User.objects.get(username=request.user)
    try:
        cart = Cart.objects.get(user=user)
    except Order.DoesNotExist:
        cart = cart.objects.create()
        cart.user = user

    content = {'cart': cart}
    template = 'shop/cart.html'

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

    item = OrderItem()
    item.product = product
    item.quantity = 1
    item.save()

    cart.item.add(item)

    return redirect('products:index')
    
