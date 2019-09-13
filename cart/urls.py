from django.urls import path

from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/<int:product_id>', views.add, name='add'),
    path('send', views.send, name='send'),
]
