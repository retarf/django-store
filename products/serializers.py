from rest_framework import serializers
from .models import Product

# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     description = serializers.CharField(style={'base_template', 'textarea.html'})
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)
# 
#     def create(self, validated_data):
#         return Product.objects.create(**validated_data)
# 
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.save()
#         return instance

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
