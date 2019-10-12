from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'products'
urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('json/', views.JsonList.as_view(), name='JsonList'),
        path('mixins/', views.JsonListMixin.as_view(), name='JsonListMixin'),
        path('<int:product_id>', views.detail, name='detail'),
        path('json/<int:product_id>', views.JsonDetail.as_view(), name='JsonDetail'),
        path('mixins/<int:pk>', views.JsonDetailMixin.as_view(), name='JsonDetailMixin'),
        path('generic/', views.JsonListGeneric.as_view(), name='JsonListGeneric'),
        path('generic/<int:pk>/', views.JsonDetailGeneric.as_view(), name='JsonDetailGeneric'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
