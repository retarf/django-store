from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User

from .models import Product
from cart.forms import CartItemForm
from cart.models import Cart, CartItem

class IndexView(generic.ListView):
    template_name = 'products/index.html'

    def get_queryset(self):
        return Product.objects.all()

def detail(request, product_id):
    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            try:
                cart = Cart.objects.get(user=user)
            except Cart.DoesNotExist:
                cart = Cart()
                cart.user = user
                cart.save()

            item = CartItem()
            item.product = product
            item.quantity = form.cleaned_data['quantity']
            item.save()

            cart.item.add(item)

            return redirect('products:index')

    else:
        form = CartItemForm()

    return render(request, 'products/detail.html', {'form': form, 'product': product})
