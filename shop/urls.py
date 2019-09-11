from django.urls import path

from . import views

#path('cart', views.CartView.as_view(), name='cart'),
app_name = 'shop'
urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('add/<int:product_id>', views.add, name='add'),
    path('user', views.show_user, name='user'),
]
