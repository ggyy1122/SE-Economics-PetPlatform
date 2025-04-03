from rest_framework import serializers
from .models import Product, Animal, Category

# 动物序列化器
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'name']

# 分类序列化器
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# 商品序列化器
class ProductSerializer(serializers.ModelSerializer):
    # 序列化 animals 和 categories 字段
    animals = AnimalSerializer(many=True)  # many=True 表示多个对象
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'stock', 'price', 'image', 'animals', 'categories']
