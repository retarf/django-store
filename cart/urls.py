from django.urls import path

from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.send, name='send'),
    path('json/', views.Cart.as_view(), name='cart'),
    path('json/<pk>', views.ItemDetail.as_view(), name='item'),
]
