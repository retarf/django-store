from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from .models import Product
from cart.forms import CartItemForm
from cart.models import CartItem

from .serializers import ProductSerializer

class IndexView(generic.ListView):
    template_name = 'products/index.html'
    queryset = Product.objects.all()

def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    user = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            item = CartItem()
            item.user = user
            item.product = product
            item.quantity = form.cleaned_data['quantity']
            item.save()

            return redirect('products:index')

    else:
        form = CartItemForm()

    return render(request, 'products/detail.html', {'form': form, 'product': product, 'user': user})


class JsonList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class JsonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
