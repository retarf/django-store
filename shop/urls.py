from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('<int:pk>', views.CartView.as_view(), name='cart'),
    path('user', views.show_user, name='user'),
]
