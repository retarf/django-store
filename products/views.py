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
from cart.models import Cart, CartItem

from .serializers import ProductSerializer

class IndexView(generic.ListView):
    template_name = 'products/index.html'

    def get_queryset(self):
        return Product.objects.all()

#@api_view(['GET', 'POST'])
#def JSONindex(request, format=None):
#    if request.method == 'GET':
#        products = Product.objects.all()
#        serializer = ProductSerializer(products, many=True)
#        return Response(serializer.data)
#
#    if request.method == 'POST':
#        serializer = ProductSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JsonList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JsonListMixin(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

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

# @api_view(['GET', 'PUT', 'DELETE'])
# def JSONdetail(request, product_id, format=None):
# 
#     try:
#         product = Product.objects.get(pk=product_id)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
# 
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
# 
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 
#     elif request.method == 'DELETE':
#         product.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

class JsonDetail(APIView):

    def get_object(self, product_id):
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, product_id, format=None):
        product = self.get_object(product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, product_id, format=None):
        product = self.get_object(product_id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id, format=None):
        product = self.get_object(product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class JsonDetailMixin(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class JsonListGeneric(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class JsonDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
