from rest_framework import serializers
from .models import Cart, CartItem
from products.models import Product

# 商品序列化器
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image']

# 购物车项序列化器
class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.ReadOnlyField(source='product.id')
    product = serializers.CharField(source='product.name')
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['product_id', 'product', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.quantity * obj.product.price

# 购物车序列化器
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']
