from django.urls import path

from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.index, name='index'),
    path('send', views.send, name='send'),
    path('json/cart', views.CartItemList.as_view(), name='item_list'),
]
