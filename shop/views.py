from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from .models import Cart

class CartView(generic.DetailView):
    template_name = 'shop/cart.html'
    model = Cart

def show_user(request):
    user = request.user
    response = "<h1>{0}</h1>".format(user)
    return HttpResponse(response)

