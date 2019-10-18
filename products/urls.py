from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'products'
urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('<int:product_id>', views.detail, name='detail'),
        path('json/', views.JsonList.as_view(), name='JsonList'),
        path('json/<pk>', views.JsonDetail.as_view(), name='JsonDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
